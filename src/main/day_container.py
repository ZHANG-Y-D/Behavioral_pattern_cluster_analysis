from datetime import date


class DayContainer:
    number_of_day: int
    date_curr: date
    pir_sensor: list  # [2880]
    temp_sensor: list  # [72][8]
    lumen_sensor: list  # [288][8]
    power_sensor: list  # [6]

    def __init__(self, date_string, num):
        self.number_of_day = num
        self.date_curr = date_string[0]
        self.pir_sensor = []
        self.lumen_sensor = []
        self.temp_sensor = []
        self.power_sensor = []

    def get_date(self):
        return self.date_curr

    def add_pir_value(self, tuple_curr):
        # TODO
        pass

    def add_temp_value(self, num_sensor, position, value):
        pass

    def add_lumen_value(self, num_sensor, position, value):
        pass

    def add_power_value(self, num_sensor, position, value):
        pass
