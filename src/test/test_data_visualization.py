from unittest import TestCase
import data_visualization as dv
import matplotlib.pyplot as plt

from day_deck import DayDeck


class Test(TestCase):
    def setUp(self):
        self.ax = plt.figure(0).subplots(2, 2)

    def test_presentation_dendrogram(self):
        linkage_list = [[0.0, 1.0, 2.0, 3.0], [2, 3, 3, 2], [4, 7, 6.2, 3], [5, 8, 13.9, 4], [6, 9, 30, 5]]
        dv.presentation_dendrogram(None, linkage_list, color_threshold=13)
        dv.show_all_figure()

    def test_presentation_common_pattern(self):
        # dv.presentation_common_pattern()
        pass

    def test_presentation_pir_list(self):
        # pir_list = ['71238', '734',
        #             '387', '7', '7', '7', '7', '7', '7', '321', '378', '78',
        #             '78', '8', '87', '73281', '83', '42', '2', '2', '2', '2',
        #             '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
        pir_list = [None, '71238', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                    '1', '1', '1', '1', '1', '1', '1', '63a', 'X', None]

        dv.presentation_pir_list(self.ax[0, 0], pir_list)
        dv.show_all_figure()

    def test_presentation_lumen_list(self):
        lumen_list = [
            [None, 'X', None, 'X', 0, 0, 0, 0, 0, 0, 0, 0, 0,
             1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3,
             3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5,
             5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7],
            [1, 1, 2, 2, 2, 2, 2, 2, 23, 3, 3, 4, 4, 5, 0, 6, 7, 0, 8, 8, None, 'X', None, 'X']]

        dv.presentation_lumen_list(self.ax[0, 1], lumen_list)
        dv.show_all_figure()

    def test_presentation_temp_list(self):
        temp_list = [[None, None, 'X', 12, 12, 12, 12, 12, 12, 12, 12, 14, 14, 14, 14, 16, 16, 16, 16,
                      16, 18, 18, 18, 18, 20, 20, 20, 20, 20, 22, 22, 22, 22, 22, 24, 24, 24, 24, 24, 26, 26, 26, 26,
                      28, 28, 28, 28, 28, 28], [None]]
        dv.presentation_temp_list(self.ax[1, 0], temp_list)
        dv.show_all_figure()

    def test_presentation_power_list(self):
        power_list = [['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
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
                       'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52, 52],
                      ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X',
                       None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                       True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                       False, False, False, False, False, False, False, False, False, False, False, False],
                      []
                      ]
        appliances_sampling_interval = [30, 120, 300, 1200, 120, 120, 120, 120, 120]
        dv.presentation_power_list(self.ax[1, 1], power_list, appliances_sampling_interval)
        dv.show_all_figure()
