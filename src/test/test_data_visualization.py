from unittest import TestCase
import data_visualization as dv
import matplotlib.pyplot as plt


class Test(TestCase):
    def test_presentation_common_pattern(self):
        # dv.presentation_common_pattern()
        pass

    def test_presentation_pir_list(self):
        # pir_list = ['71238', '734',
        #             '387', '7', '7', '7', '7', '7', '7', '321', '378', '78',
        #             '78', '8', '87', '73281', '83', '42', '2', '2', '2', '2',
        #             '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2', '2']
        pir_list = ['71238', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1',
                    '1', '1', '1', '1', '1', '1', '1', '63a']

        dv.presentation_pir_list(plt.figure(0), pir_list)
        dv.show_all_figure()
