class ProximityMatrix:
    proximity_matrix: list

    def __init__(self):
        self.proximity_matrix = []

    def add_distance(self, x_axis, y_axis, distance):
        if self.proximity_matrix[x_axis][y_axis] is None:
            self.proximity_matrix[x_axis][y_axis] = distance
        else:
            pass

    @staticmethod
    def calculate_manhattan_distance(first_matrix, second_matrix):
        distance = 0
        if ProximityMatrix.is_2d_list(first_matrix):
            for i in range(len(first_matrix)):
                distance = \
                    ProximityMatrix.calculate_1d_distance(first_matrix[i], second_matrix[i]) \
                    + distance
            return distance
        else:
            return ProximityMatrix.calculate_1d_distance(first_matrix, second_matrix)

    @staticmethod
    def calculate_1d_distance(ele_first, ele_second):
        distance = 0
        for i in range(len(ele_first)):
            if ele_first[i] != ele_second[i]:
                distance += 1
        return distance

    @staticmethod
    def is_2d_list(matrix_list):
        if isinstance(matrix_list[0], list):
            return True
        else:
            return False
