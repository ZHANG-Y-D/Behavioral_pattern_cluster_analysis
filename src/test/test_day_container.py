from datetime import date, datetime
from unittest import TestCase
from day_container import DayContainer


class TestDayContainer(TestCase):

    def setUp(self):
        self.day = DayContainer(date(2020, 4, 2), 8)

    def test_find_index(self):
        index = self.day.find_index(datetime(2020, 4, 2, 0, 0, 30), datetime(2020, 4, 2, 0, 16, 49))
        self.assertEqual(index, 1)

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
        self.day.add_pir_value((3, datetime(2020, 4, 2, 0, 4, 10), datetime(2020, 4, 2, 0, 4, 10)))
        self.day.add_pir_value((None, datetime(2020, 4, 2, 0, 4, 10), datetime(2020, 4, 2, 0, 4, 10)))
        print(self.day.get_pir_list())
        self.day.fill_black()
        print(self.day.get_pir_list())
        self.assertEqual(self.day.get_pir_list()[7], '3')
        self.assertEqual(self.day.get_pir_list()[8], '3f')
        self.assertEqual(self.day.get_pir_list()[9], 'f')

