class ProximityMatrix:
    proximity_matrix: list

    def __init__(self):
        pass

    def init_proximity_matrix(self, length):
        self.proximity_matrix = [None] * (length - 1)
        length_of_every_list = length - 1
        for i in range(length - 1):
            self.proximity_matrix[i] = [None] * length_of_every_list
            length_of_every_list -= 1

    def add_distance(self, x_axis, y_axis, day_container, later_day_container):
        distance = ProximityMatrix.sum_all_list_distance(day_container, later_day_container)
        self.proximity_matrix[x_axis][y_axis] = distance

    def get_proximity_matrix(self):
        return self.proximity_matrix

    def find_min_coordinate(self):
        min_value = min([min(ele) for ele in self.proximity_matrix])
        for i, ele_x in enumerate(self.proximity_matrix):
            for j, ele_y in enumerate(self.proximity_matrix[i]):
                if ele_y == min_value:
                    return [i, j]

    @staticmethod
    def is_2d_list(matrix_list):
        if isinstance(matrix_list[0], list):
            return True
        else:
            return False

    @staticmethod
    def calculate_1d_distance(ele_first, ele_second):
        distance = 0
        for i in range(len(ele_first)):
            if ele_first[i] != ele_second[i]:
                distance += 1
        return distance

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
    def sum_all_list_distance(day_container, later_day_container):
        distance = 0
        for i in range(len(day_container.get_all_list())):
            if day_container.get_all_list()[i] is not None:
                distance = ProximityMatrix.calculate_manhattan_distance(day_container.get_all_list()[i],
                                                                        later_day_container.get_all_list()[i]) \
                           + distance

        return distance
