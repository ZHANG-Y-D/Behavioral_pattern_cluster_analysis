from datetime import date, datetime
from unittest import TestCase
from day_container import DayContainer


class TestDayContainer(TestCase):

    appliances_sampling_interval = [30, 120, 300, 1200, 120, 120, 120, 120, 120]

    def setUp(self):
        self.day = DayContainer(date(2020, 4, 2), 8)
        self.assertEqual(8, self.day.date_num)
        self.day.init_pir_list(2880)
        self.day.init_lumen_list(288)
        self.day.init_temp_list(72)
        self.day.init_power_list(self.appliances_sampling_interval)

    def test_find_index(self):
        index = self.day.find_index(datetime(2020, 4, 2, 0, 0, 30), 30)
        self.assertEqual(index, 1)
        index = self.day.find_index(datetime(2020, 4, 2, 0, 1, 0), 300)
        self.assertEqual(index, 0)
        index = self.day.find_index(datetime(2020, 4, 2, 0, 5, 0), 300)
        self.assertEqual(index, 1)
        index = self.day.find_index(datetime(2020, 4, 2, 0, 4, 0), 120)
        self.assertEqual(index, 2)
        index = self.day.find_index(datetime(2020, 4, 2, 0, 10, 0), 120)
        self.assertEqual(index, 5)
        index = self.day.find_index(datetime(2020, 4, 2, 1, 10, 0), 120)
        self.assertEqual(index, 35)
        index = self.day.find_index(datetime(2020, 4, 2, 1, 00, 0), 1200)
        self.assertEqual(index, 3)
        index = self.day.find_index(datetime(2020, 4, 2, 23, 58, 0), 120)
        self.assertEqual(index, 719)
        index = self.day.find_index(datetime(2020, 4, 2, 23, 55, 0), 300)
        self.assertEqual(index, 287)

    def test_add_pir_value(self):
        self.day.add_pir_value((3, datetime(2020, 4, 2, 10, 0, 10), datetime(2020, 4, 2, 10, 0, 20)))
        print(self.day.get_pir_list())
        self.day.add_pir_value((3, datetime(2020, 4, 2, 10, 0, 10), datetime(2020, 4, 2, 10, 2, 20)))
        print(self.day.get_pir_list())
        self.day.add_pir_value((10, datetime(2020, 4, 2, 5, 0, 10), datetime(2020, 4, 2, 5, 2, 20)))
        print(self.day.get_pir_list())
        self.day.add_pir_value((None, datetime(2020, 4, 2, 1, 0, 10), datetime(2020, 4, 2, 1, 2, 20)))
        print(self.day.get_pir_list())
        self.day.add_pir_value((3, datetime(2020, 4, 2, 0, 4, 10), datetime(2020, 4, 2, 0, 4, 10)))
        print(self.day.get_pir_list())
        self.assertEqual(self.day.get_pir_list()[8], '3')

    def test_fill_black(self):
        self.day.add_pir_value((None, datetime(2020, 4, 2, 0, 4, 10), datetime(2020, 4, 5, 0, 4, 10)))
        self.day.fill_black_for_pir_list()
        self.assertEqual(None, self.day.get_pir_list()[2879])
        print(self.day.get_pir_list())
        self.day.add_pir_value((3, datetime(2020, 4, 2, 0, 4, 10), datetime(2020, 4, 2, 0, 4, 10)))
        self.day.add_pir_value((None, datetime(2020, 4, 2, 0, 4, 10), datetime(2020, 4, 2, 0, 4, 10)))
        print(self.day.get_pir_list())
        self.day.fill_black_for_pir_list()
        print(self.day.get_pir_list())
        self.assertEqual(self.day.get_pir_list()[7], '3')
        self.assertEqual(self.day.get_pir_list()[8], '3f')
        self.assertEqual(self.day.get_pir_list()[9], 'f')

    def test_normalisation_time(self):
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 1, 5, 10), 120)
        self.assertEqual(return_value, datetime(2020, 4, 2, 1, 4, 00))
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 1, 23, 10), 300)
        self.assertEqual(return_value, datetime(2020, 4, 2, 1, 20, 00))
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 1, 0, 10), 300)
        self.assertEqual(return_value, datetime(2020, 4, 2, 1, 0, 00))
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 1, 55, 10), 1200)
        self.assertEqual(return_value, datetime(2020, 4, 2, 1, 40, 00))
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 1, 0, 10), 30)
        self.assertEqual(return_value, datetime(2020, 4, 2, 1, 0, 00))
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 23, 59, 59), 300)
        self.assertEqual(return_value, datetime(2020, 4, 2, 23, 55, 00))
        return_value = self.day.normalisation_time(None, datetime(2020, 4, 2, 23, 59, 59), 1200)
        self.assertEqual(return_value, datetime(2020, 4, 2, 23, 40, 00))

    def test_add_lumen_value(self):
        self.day.add_lumen_value((10, '20', datetime(2020, 4, 2, 0, 10, 0)))
        self.assertEqual(2, self.day.get_lumen_list()[9][2])
        self.day.add_lumen_value((10, '20', datetime(2020, 4, 2, 23, 59, 59)))
        self.assertEqual(2, self.day.get_lumen_list()[9][287])
        self.assertEqual(None, self.day.get_lumen_list()[8][287])
        self.day.add_lumen_value((1, '200', datetime(2020, 4, 2, 23, 59, 59)))
        self.assertEqual(4, self.day.get_lumen_list()[0][287])

    def test_determine_temp_level(self):
        return_value = self.day.determine_temp_level(19.6)
        self.assertEqual(18, return_value)
        return_value = self.day.determine_temp_level(-19.6)
        self.assertEqual(-20, return_value)
        return_value = self.day.determine_temp_level(0.2)
        self.assertEqual(0, return_value)
        return_value = self.day.determine_temp_level(-1.2)
        self.assertEqual(-2, return_value)
        return_value = self.day.determine_temp_level(1.2)
        self.assertEqual(0, return_value)
        return_value = self.day.determine_temp_level(17.2)
        self.assertEqual(16, return_value)

    def test_determine_power_level(self):
        return_value = self.day.determine_power_level(24, 0, 5)
        self.assertEqual(False, return_value)
        return_value = self.day.determine_power_level(150, 0, 0)
        self.assertEqual(False, return_value)
        return_value = self.day.determine_power_level(150, 2, 1)
        self.assertEqual(True, return_value)
        return_value = self.day.determine_power_level(45, 3, 0)
        self.assertEqual(3, return_value)
        return_value = self.day.determine_power_level(32, 0, 0)
        self.assertEqual(0, return_value)
        return_value = self.day.determine_power_level(32, 2, 0)
        self.assertEqual(0, return_value)
        return_value = self.day.determine_power_level(32, 5, 0)
        self.assertEqual(1, return_value)
        return_value = self.day.determine_power_level(32, 50, 0)
        self.assertEqual(1, return_value)
        return_value = self.day.determine_power_level(32, 51, 0)
        self.assertEqual(2, return_value)

    def test_add_power_value(self):
        self.day.add_power_value((24, 1, 20, datetime(2020, 4, 2, 0, 10, 0)), self.appliances_sampling_interval)
        self.assertEqual(False, self.day.get_power_list()[0][20])
        self.day.add_power_value((32, 50, 0, datetime(2020, 4, 2, 0, 10, 0)), self.appliances_sampling_interval)
        self.assertEqual(1, self.day.get_power_list()[3][0])
        self.day.add_power_value((45, 5, 0, datetime(2020, 4, 2, 0, 10, 0)), self.appliances_sampling_interval)
        self.assertEqual(5, self.day.get_power_list()[6][5])
        # for ele in self.day.get_power_list():
        #     print(ele)

