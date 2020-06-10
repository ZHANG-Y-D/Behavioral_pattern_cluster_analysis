from unittest import TestCase
import matplotlib.pyplot as plt
import data_visualization as dv
from day_container import DayContainer
from day_deck import DayDeck
from datetime import date


class Test(TestCase):
    def setUp(self):
        pass

    def test_presentation_dendrogram(self):
        linkage_list = [[0.0, 1.0, 2.0, 3.0], [2, 3, 3, 2], [4, 7, 6.2, 3], [5, 8, 13.9, 4], [6, 9, 30, 5]]
        dv.presentation_dendrogram(None, linkage_list, 14, )
        dv.show_all_figure()

    def test_presentation_calendar(self):
        link_color = {'icoord': [[15.0, 15.0, 25.0, 25.0],
                                 [5.0, 5.0, 20.0, 20.0],
                                 [45.0, 45.0, 55.0, 55.0],
                                 [65.0, 65.0, 75.0, 75.0],
                                 [50.0, 50.0, 70.0, 70.0],
                                 [35.0, 35.0, 60.0, 60.0],
                                 [12.5, 12.5, 47.5, 47.5]],
                      'dcoord': [[0.0, 1853.0, 1853.0, 0.0],
                                 [0.0, 2526.0, 2526.0, 1853.0],
                                 [0.0, 1428.0, 1428.0, 0.0],
                                 [0.0, 1606.0, 1606.0, 0.0],
                                 [1428.0, 2280.0, 2280.0, 1606.0],
                                 [0.0, 2700.0, 2700.0, 2280.0],
                                 [2526.0, 2867.0, 2867.0, 2700.0]],
                      'ivl': ['2021-04-08', '2019-04-06', '2022-04-07', '2020-04-01',
                              '2022-04-03', '2020-04-04', '2020-04-02', '2020-04-05'],
                      'leaves': [7, 5, 6, 0, 2, 3, 1, 4],
                      'color_list': ['g', 'b', 'r', 'c', 'b', 'b', 'b']}
        dv.presentation_calendar(link_color)
        dv.show_all_figure()

    def test_presentation_pir_list(self):
        self.ax = plt.figure().subplots(2, 2)

        # pir_list = ['71238', '734',
        #             '387', '7', '7', '7', '7', '7', '7', '321', '378', '78',
        #             '78', '8', '87', '73281', '83', '42', '2', '2', '2', '2',
        #             '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
        pir_list = [None, '71238', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                    '1', '1', '1', '1', '1', '1', '1', '63a', 'X', None]

        dv.presentation_pir_list(self.ax[0, 0], pir_list)
        dv.show_all_figure()

    def test_presentation_lumen_list(self):
        self.ax = plt.figure().subplots(2, 2)

        lumen_list = [
            [None, 'X', None, 'X', 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
             3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5,
             5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7],
            [1, 1, 2, 2, 2, 2, 2, 2, 23, 3, 3, 4, 4, 5, 0, 6, 7, 0, 8, 8, None, 'X', None, 'X']]

        dv.presentation_lumen_list(self.ax[0, 1], lumen_list)
        dv.show_all_figure()

    def test_presentation_temp_list(self):
        self.ax = plt.figure().subplots(2, 2)

        temp_list = [[None, None, 'X', 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16,
                      16, 18, 18, 18, 18, 20, 20, 20, 20, 20, 22, 22, 22, 22, 22, 24, 24, 24, 24, 24, 26, 26, 26, 26,
                      28, 28, 28, 28, 28, 28], [None]]
        dv.presentation_temp_list(self.ax[1, 0], temp_list)
        dv.show_all_figure()

    def test_presentation_power_list(self):
        self.ax = plt.figure().subplots(2, 2)

        power_list = [[True, False, True, False, True, False, True, False, True, False, True, False, True, False,
                       True, False, True, False, True, False, True, False, True, False, True, False, True, False,
                       True, False, True, False, True, False, True, False, True, False, True, False, True, False,
                       True, False, True, False, True, False, True, False, True, False,True, False, True, False, False],

                      [True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],

                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],

                      [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 5, 5, 5, 50, 50, 50, 50, 50, 50, 50,
                       'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],

                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
                       1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 5, 50, 50, 50, 50, 50, 50, 50,
                       52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52,
                       'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],

                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],
                      []
                      ]
        # appliances_sampling_interval = [30, 120, 300, 1200, 120, 120, 120, 120, 120]
        appliances_sampling_interval = [1200, 1006, 1006, 1006, 1006, 1006, 1006, 1006, 1006]
        dv.presentation_power_list(self.ax[1, 1], power_list, appliances_sampling_interval)
        dv.show_all_figure()
