from datetime import time, timedelta, date


class DayContainer:
    date_num: int
    date_curr: date
    pir_sensor: list  # length 2880.
    lumen_sensor: list  # [10][288] every 5 minute
    temp_sensor: list  # [10][72] every 20 minute
    power_sensor: list
    appliances_sampling_interval: list

    def __init__(self, date_curr, num):
        self.date_curr = date_curr
        self.date_num = num

    def modify_date_num(self, num):
        self.date_num = num

    def init_pir_list(self, sampling_interval):
        self.pir_sensor = [None] * sampling_interval

    def init_lumen_list(self, sampling_interval):
        self.lumen_sensor = [[None] * sampling_interval for i in range(10)]

    def init_temp_list(self, sampling_interval):
        self.temp_sensor = [[None] * sampling_interval for i in range(10)]

    def init_power_list(self, appliances_sampling_interval):
        """
            There are 9 domestic appliances
            1.Microonde: No.24, sampling interval is 30s
            2.Televisione: No.26, sampling interval is 120s
            3.HC2 Power: No.28, sampling interval is 300s
            4.Frigorifero: No.32, sampling interval is 1200s
                            Power_level: 0w, 2w, 50w
            5.Forno: No.34, sampling interval is 120s
            6.Lavatrici: No.36, sampling interval is 120s
            7.Serra A: No.45, sampling interval is 120s,
                        Directly record the original value
            8.Lavastoviglie: No.148, sampling interval is 120s
            9.PC: No.150, sampling interval is 120s, threshold: 5w
        """
        self.power_sensor = [None] * 9
        self.power_sensor[0] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[0])  # Microonde
        self.power_sensor[1] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[1])  # Televisione
        self.power_sensor[2] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[2])  # HC2 Power
        self.power_sensor[3] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[3])  # Frigorifero
        self.power_sensor[4] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[4])  # Forno
        self.power_sensor[5] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[5])  # Lavatrici
        self.power_sensor[6] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[6])  # Serra A
        self.power_sensor[7] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[7])  # Lavastoviglie
        self.power_sensor[8] = \
            [None] * int((60 * 60 * 24) / appliances_sampling_interval[8])  # PC

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
        time_curr = self.normalisation_time(None, tuple_curr[2], 300)
        index = self.find_index(time_curr, 300)
        self.lumen_sensor[tuple_curr[0] - 1][index] = lumen_level

    def add_temp_value(self, tuple_curr):
        temp_level = self.determine_temp_level(tuple_curr[1])
        time_curr = self.normalisation_time(None, tuple_curr[2], 1200)
        index = self.find_index(time_curr, 1200)
        self.temp_sensor[tuple_curr[0] - 1][index] = temp_level

    def add_power_value(self, tuple_curr, appliances_sampling_interval):
        power_level = self.determine_power_level(tuple_curr[0], tuple_curr[1], tuple_curr[2])
        power_position = self.normalisation_power_position_in_list(tuple_curr[0])
        time_curr = self.normalisation_time(None,
                                            tuple_curr[3],
                                            appliances_sampling_interval[power_position])
        index = self.find_index(time_curr, appliances_sampling_interval[power_position])
        self.power_sensor[power_position][index] = power_level

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
                print("Warning: No PIR signal received at "
                      + self.get_date().strftime("%Y-%m-%d"))
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

    def fill_black_for_list(self, list_type):
        """
        It is used to fill in the curr_list blanks,
        the previous signal will use to be Filler.
        if the first signal is black, Fill with
        the following "not black signal"
        [None,None,'3','4','3',None,None,'5','4,.......]
        -> ['3','3','3','4','3','3','3','5','4',.......]
        if the whole curr_list is None(initial state),
        this function will do nothing.

        :param list_type: which curr_list you want to fill
                        lumen temp or power

        """
        if list_type == 'lumen':
            fill_list = self.lumen_sensor
        elif list_type == 'temp':
            fill_list = self.temp_sensor
        elif list_type == 'power':
            fill_list = self.power_sensor
        else:
            print("Warning: list_type have to be lumen temp or power")
            return

        num_signal = 0
        for curr_list in fill_list:
            num_signal += 1
            index = 0
            fill_value = None
            if curr_list[0] is None:
                for signal in curr_list:
                    if signal is not None:
                        fill_value = signal
                        break
                    index += 1
                if fill_value is None:
                    print("Warning: Room " + str(num_signal) + " No " + list_type
                          + " signal received at " + self.get_date().strftime("%Y-%m-%d"))
                    continue
                for i in range(index):
                    curr_list[i] = fill_value

            index = 0
            for signal in curr_list:
                if signal is None:
                    curr_list[index] = curr_list[index - 1]
                index += 1

    def get_date(self):
        return self.date_curr

    def get_pir_list(self):
        try:
            return self.pir_sensor
        except AttributeError:
            return None

    def get_lumen_list(self):
        try:
            return self.lumen_sensor
        except AttributeError:
            return None

    def get_temp_list(self):
        try:
            return self.temp_sensor
        except AttributeError:
            return None

    def get_power_list(self):
        try:
            return self.power_sensor
        except AttributeError:
            return None

    def get_all_list(self):
        all_list = \
            [self.get_pir_list(), self.get_lumen_list(), self.get_temp_list(), self.get_power_list()]
        return all_list

    @staticmethod
    def determine_temp_level(value):
        """
            We temporarily set the temperature to two degrees as a step
            For example：
                18.5 -> 18
                19.5 -> 18
                They are regarded as no difference,
                because they are in the same step
        """
        value = int(float(value))
        return value - (value % 2)

    @staticmethod
    def determine_power_level(num_of_appliance, value, threshold):
        """
            For all appliances except refrigerators,Serra A,
            We use True and False to indicate on/off,
            Above the threshold is on and vice versa.
            Attention: PC has no threshold in sql, but we use 5w
            For refrigerators, we use power_level [0,2,50] -> 0,1,2
            For Serra A, we use the original value of sql
        """
        power_level_for_refrigerator = [0, 2, 50]
        threshold = int(threshold)
        value = int(value)

        if num_of_appliance == 150 and threshold == 0:  # For PC
            threshold = 5

        if threshold != 0:
            if value > threshold:
                return True
            else:
                return False
        elif num_of_appliance == 45:  # For Serra A
            return value
        elif num_of_appliance == 32:
            if power_level_for_refrigerator[0] <= value <= power_level_for_refrigerator[1]:
                return 0
            elif power_level_for_refrigerator[1] < value <= power_level_for_refrigerator[2]:
                return 1
            else:
                return 2
        else:
            print("Warning: Do not have this appliance, Maybe the database has changed")

    @staticmethod
    def normalisation_power_position_in_list(num_of_appliance):
        """
            Determine where appliances are stored in the list
        """
        if num_of_appliance == 24:
            return 0
        elif num_of_appliance == 26:
            return 1
        elif num_of_appliance == 28:
            return 2
        elif num_of_appliance == 32:
            return 3
        elif num_of_appliance == 34:
            return 4
        elif num_of_appliance == 36:
            return 5
        elif num_of_appliance == 45:
            return 6
        elif num_of_appliance == 148:
            return 7
        elif num_of_appliance == 150:
            return 8
        else:
            print("Warning: Do not have this appliance, Maybe the database has changed")
