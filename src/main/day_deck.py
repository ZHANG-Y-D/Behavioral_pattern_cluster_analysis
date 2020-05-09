import copy

from day_container import DayContainer
from proximity_matrix import ProximityMatrix


class DayDeck:
    data_name_labels: list
    dayDeck: list
    date_num_of_clustering: int

    def __init__(self):
        self.dayDeck = []
        self.data_name_labels = []

    def add_date(self, date_to_day_container, num):
        self.dayDeck.append(DayContainer(date_to_day_container, num))
        self.data_name_labels.append(str(date_to_day_container))

    def init_num_of_clustering(self, num):
        self.date_num_of_clustering = num

    def get_list_of_day(self):
        return self.dayDeck

    def clustering(self, first_day, second_day):
        after_clustering = copy.deepcopy(first_day)

        # Modify date number for clustering
        after_clustering.date_num = self.date_num_of_clustering
        self.date_num_of_clustering += 1

        # Add total number clustered element
        after_clustering.num_of_clustered = first_day.num_of_clustered + second_day.num_of_clustered

        # Cluster all available list for two days
        if first_day.get_pir_list() and second_day.get_pir_list() is not None:
            after_clustering.pir_sensor = \
                DayDeck.cluster_two_list(first_day.get_pir_list(), second_day.get_pir_list())

        if first_day.get_lumen_list() and second_day.get_lumen_list() is not None:
            after_clustering.lumen_sensor = \
                DayDeck.cluster_two_list(first_day.get_lumen_list(), second_day.get_lumen_list())

        if first_day.get_temp_list() and second_day.get_temp_list() is not None:
            after_clustering.temp_sensor = \
                DayDeck.cluster_two_list(first_day.get_temp_list(), second_day.get_temp_list())

        if first_day.get_power_list() and second_day.get_power_list() is not None:
            after_clustering.power_sensor = \
                DayDeck.cluster_two_list(first_day.get_power_list(), second_day.get_power_list())

        self.dayDeck.append(after_clustering)

    @staticmethod
    def cluster_two_list(f_list, s_list):
        clustered_list = copy.deepcopy(f_list)

        if not ProximityMatrix.is_2d_list(f_list):  # For pir matrix
            clustered_list = DayDeck.cluster_1d_list(f_list, s_list)
        else:  # For lumen/temp/power matrix
            for i in range(len(f_list)):
                clustered_list[i] = \
                    DayDeck.cluster_1d_list(f_list[i], s_list[i])

        return clustered_list

    @staticmethod
    def cluster_1d_list(f_list, s_list):
        clustered_list = copy.deepcopy(f_list)
        for i in range(len(f_list)):
            if f_list[i] == 'X' or s_list[i] == 'X' \
                    or f_list[i] != s_list[i]:
                clustered_list[i] = 'X'

        return clustered_list
