from unittest import TestCase
from day_deck import DayDeck


class TestDayDeck(TestCase):

    def setUp(self):
        self.day_deck = DayDeck()

    def test_cluster_two_list(self):
        list_1d_a = [1, 2, 3, 3, 5, 6, 9, 10]
        list_1d_b = [1, 2, 3, 4, 5, 6, 9, 8]
        return_value = self.day_deck.cluster_two_list(list_1d_a, list_1d_b)
        self.assertEqual([1, 2, 3, 'X', 5, 6, 9, 'X'], return_value)

        list_1d_a = [1, 2, 3, 3, 5, 6, 'X', 'X']
        list_1d_b = [1, 2, 3, 4, 5, 6, 9, 'X']
        return_value = self.day_deck.cluster_two_list(list_1d_a, list_1d_b)
        self.assertEqual([1, 2, 3, 'X', 5, 6, 'X', 'X'], return_value)

        list_2d_a = [['X', 2, 3, 4, 5, 6, 7],
                     [1, 2, 3, 4, 5, 6, 7],
                     [1, 2, 3, 4, 5, 6, 7],
                     [None, 'X', 3, 4, 5, 6, 7]]
        list_2d_b = [[1, 2, 3, 4, 5, 6, 7],
                     [1, 2, 3, 4, 5, 6, 7],
                     [1, 2, 3, 4, 5, 6, 7],
                     [None, 'X', 3, 4, 5, 6, 10]]
        return_value = self.day_deck.cluster_two_list(list_2d_a, list_2d_b)
        assert_list = [['X', 2, 3, 4, 5, 6, 7],
                       [1, 2, 3, 4, 5, 6, 7],
                       [1, 2, 3, 4, 5, 6, 7],
                       [None, 'X', 3, 4, 5, 6, 'X']]
        self.assertEqual(assert_list, return_value)
