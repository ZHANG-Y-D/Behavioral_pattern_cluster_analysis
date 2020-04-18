from datetime import datetime
from datetime import timedelta
from datetime import date


class DayContainer:
    number_of_day: int
    date_curr: date
    pir_sensor: list  # length 2880.
    temp_sensor: list  # [72][8]
    lumen_sensor: list  # [288][8]
    power_sensor: list  # [6]

    def __init__(self, date_curr, num):
        self.number_of_day = num
        self.date_curr = date_curr
        self.pir_sensor = [None] * 2880
        self.lumen_sensor = []
        self.temp_sensor = []
        self.power_sensor = []

    def get_date(self):
        return self.date_curr

    def add_pir_value(self, tuple_curr):
        """
            id_room from 1 to 10. We use hexadecimal to represent，
            which is 1 2 3 4 5 6 7 8 9 a, a is 10.
            When not at home, we use f to indicate
            When there are two states at the same time,
            we directly add it.
            For example: pir 1 on and then 10 on, write 1a
            If a tuple spans more than two days, it is directly regarded as noise
        """

        if tuple_curr[2].date() - tuple_curr[1].date() > timedelta(days=1):
            return

        room = tuple_curr[0]
        if room is None:
            room = 'f'
        elif room == 10:
            room = 'a'
        room = str(room)

        t_from = self.normalisation_time(tuple_curr[1])
        t_to = self.normalisation_time(tuple_curr[2])

        while True:
            index = self.find_index(t_from, t_to)
            if index == -1:
                return
            if self.pir_sensor[index] is None:
                self.pir_sensor[index] = room
            else:
                self.pir_sensor[index] = "{0}{1}".format(self.pir_sensor[index], room)

            t_from = t_from + timedelta(seconds=30)

    def get_pir_list(self):
        return self.pir_sensor

    def add_temp_value(self, num_sensor, position, value):
        pass

    def add_lumen_value(self, num_sensor, position, value):
        pass

    def add_power_value(self, num_sensor, position, value):
        pass

    def find_index(self, t_from, t_to):
        if t_from.time() > t_to.time() \
                or t_from.date() > self.date_curr:
            return -1
        index = t_from.hour * 120
        index = t_from.minute * 2 + index
        if t_from.second >= 30:
            index += 1
        return index

    def normalisation_time(self, time_value):
        if time_value.date() < self.date_curr:
            time_value = time_value.replace(year=self.date_curr.year,
                                            month=self.date_curr.month,
                                            day=self.date_curr.day,
                                            hour=0,
                                            minute=0,
                                            second=0)
        elif time_value.date() > self.date_curr:
            time_value = time_value.replace(year=self.date_curr.year,
                                            month=self.date_curr.month,
                                            day=self.date_curr.day,
                                            hour=23,
                                            minute=59,
                                            second=30)
        else:
            if time_value.second < 30:
                time_value = time_value.replace(second=0)
            else:
                time_value = time_value.replace(second=30)

        return time_value
