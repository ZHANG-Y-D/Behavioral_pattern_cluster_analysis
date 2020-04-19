from datetime import datetime, time
from datetime import timedelta
from datetime import date


class DayContainer:
    number_of_day: int
    date_curr: date
    pir_sensor: list  # length 2880.
    lumen_sensor: list  # [10][288]
    temp_sensor: list  # [72][8]
    power_sensor: list  # [6]

    def __init__(self, date_curr, num):
        self.number_of_day = num
        self.date_curr = date_curr
        self.pir_sensor = [None] * 2880
        self.lumen_sensor = [[None] * 288 for i in range(10)]
        self.temp_sensor = []
        self.power_sensor = []

    def get_date(self):
        return self.date_curr

    def get_lumen_list(self):
        return self.lumen_sensor

    def add_pir_value(self, tuple_curr):
        """
            id_room from 1 to 10. We use a to represent 10，
            which is 1 2 3 4 5 6 7 8 9 a, a is 10.
            When not at home, we use f to represent
            When there are two states at the same time,
            we directly append it,but the same signal is only recorded once at the same time.
                For example: pir 1 on and then 10 on, write 1a,
                but 1 on f on and then f on, write 1f.
            If a tuple spans more than two days, treat it directly as noise
            Finally, a loop is used to fill in the blanks,
            the last char of the previous signal will use to be Filler.
            if the first signal is black, Fill with the first char of the following "not black signal"
                For example: previous is '34', we just use '4',
                Because signal 4 is the last presented.
                And
                [None,None,'34','4','43',None,None,'54','4,.......]
                -> ['3','3','34','4','43','3','3','54','4',.......]
        """
        if tuple_curr[2].date() - tuple_curr[1].date() > timedelta(days=1):
            return

        room = tuple_curr[0]
        if room is None:
            room = 'f'
        elif room == 10:
            room = 'a'
        room = str(room)

        t_from = self.normalisation_time(self.date_curr, tuple_curr[1], 30)
        t_to = self.normalisation_time(self.date_curr, tuple_curr[2], 30)

        while True:
            if t_from.time() > t_to.time() \
                    or t_from.date() > self.date_curr:
                break
            index = self.find_index(t_from, 30)
            if self.pir_sensor[index] is None:
                self.pir_sensor[index] = room
            else:
                # the same signal is only recorded once at the same time.
                if room not in self.pir_sensor[index]:
                    self.pir_sensor[index] = "{0}{1}".format(self.pir_sensor[index], room)
            # Record every 30 seconds
            t_from = t_from + timedelta(seconds=30)

    def add_lumen_value(self, tuple_curr):
        lumen_level = self.determine_lumen_level(tuple_curr[1], tuple_curr[2])
        time_curr = self.normalisation_time(None, tuple_curr[2], 30)
        index = self.find_index(time_curr, 5 * 60)
        self.lumen_sensor[tuple_curr[0] - 1][index] = lumen_level

    def get_pir_list(self):
        return self.pir_sensor

    def add_temp_value(self, num_sensor, position, value):
        pass

    def add_power_value(self, num_sensor, position, value):
        pass

    @staticmethod
    def find_index(t_from, sampling_interval):
        # Sampling_interval unit is second.
        index = t_from.hour * 3600 / sampling_interval
        index = int(t_from.minute * 60 / sampling_interval) + index
        if sampling_interval <= 60 and t_from.second >= 30:
            index += 1
        return int(index)

    @staticmethod
    def normalisation_time(date_curr, time_value, sampling_interval):
        """
            Sampling_interval unit is second.
            The sampling interval is
                pir 30s
                lumen 300s
                temp 1200s
        """
        if date_curr is None or time_value.date() == date_curr:
            if sampling_interval >= 60:
                time_value = time_value.replace(second=0)
                time_value = time_value.replace(minute=
                                                time_value.minute -
                                                time_value.minute %
                                                int(sampling_interval / 60))
            else:
                if time_value.second < 30:
                    time_value = time_value.replace(second=0)
                else:
                    time_value = time_value.replace(second=30)
        elif time_value.date() < date_curr:
            time_value = time_value.replace(year=date_curr.year,
                                            month=date_curr.month,
                                            day=date_curr.day,
                                            hour=0,
                                            minute=0,
                                            second=0)
        else:
            time_value = time_value.replace(year=date_curr.year,
                                            month=date_curr.month,
                                            day=date_curr.day,
                                            hour=23,
                                            minute=59,
                                            second=30)

        return time_value

    def fill_black_for_pir_list(self):
        """
        It is used to fill in the pir list blanks,
        the last char of the previous signal will use to be Filler.
        if the first signal is black, Fill with the first char of
        the following "not black signal"
            For example: previous is '34', we just use '4',
            Because signal 4 is the last presented.
            And
            [None,None,'34','4','43',None,None,'54','4,.......]
            -> ['3','3','34','4','43','3','3','54','4',.......]
        """
        index = 0
        fill_value = None
        if self.get_pir_list()[0] is None:
            for signal in self.get_pir_list():
                if signal is not None:
                    fill_value = signal[0]
                    break
                index += 1
            if fill_value is None:
                return
            for i in range(index):
                self.pir_sensor[i] = fill_value

        index = 0
        for signal in self.get_pir_list():
            if signal is None:
                self.pir_sensor[index] = \
                    self.get_pir_list()[index - 1][-1]
            index += 1

    @staticmethod
    def determine_lumen_level(value, time_curr):
        """
         We determine the lumen level according to sunrise and sunset，
         The sunrise and sunset times for Milan in April are from 6:30~20:00
         Lumen level is from 0 to 5 (whitch is from 'buio' to 'ottima')
         Day is 0 20 40 150 300
         Night is 0 5 20 110 200
        """
        value = int(value)
        day_level = [0, 20, 40, 150, 300]
        night_level = [0, 5, 20, 110, 200]
        if time(6, 30, 00) < time_curr.time() <= time(20, 00, 00):
            level = day_level
        else:
            level = night_level

        if value == level[0]:
            return 0
        elif level[0] < value <= level[1]:
            return 1
        elif level[1] < value <= level[2]:
            return 2
        elif level[2] < value <= level[3]:
            return 3
        elif level[3] < value <= level[4]:
            return 4
        else:
            return 5
