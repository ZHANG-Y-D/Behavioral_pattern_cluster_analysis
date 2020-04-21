from unittest import TestCase
from proximity_matrix import ProximityMatrix


class TestProximityMatrix(TestCase):

    def setUp(self):
        self.proximity_matrix = ProximityMatrix()

    def test_calculate_distance(self):
        print("asd")

    def test_calculate_1d_distance(self):
        list_1d_a = [1, 2, 3, 3, 5, 6, True]
        list_1d_b = [1, 2, 3, 4, 5, 6, False]
        return_value = ProximityMatrix.calculate_1d_distance(list_1d_a, list_1d_b)
        self.assertEqual(2, return_value)

    def test_calculate_manhattan_distance(self):
        list_1d_a = [1, 2, 3, 3, 5, 6, True]
        list_1d_b = [1, 2, 3, 4, 5, 6, False]
        return_value = ProximityMatrix.calculate_manhattan_distance(list_1d_a, list_1d_b)
        self.assertEqual(2, return_value)
        list_2d_a = [[1, 2, 3, 4, 5, 6, 7],
                          [1, 2, 3, 4, 5, 6, 7],
                          [1, 2, 3, 4, 5, 6, 7],
                          [1, 2, 3, 4, 5, 6, 7]]
        list_2d_b = [[1, 2, 3, 4, 5, 6, 7],
                          [1, 2, 3, 4, 5, 6, 7],
                          [1, 2, 3, 4, 5, 6, 7],
                          [1, 2, 3, 4, 5, 6, 7]]
        return_value = ProximityMatrix.calculate_manhattan_distance(list_2d_a, list_2d_b)
        self.assertEqual(0, return_value)

