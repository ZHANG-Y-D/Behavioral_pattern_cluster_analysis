from day_container import DayContainer


class DayDeck:
    dayDeck: list
    num_of_clustering: int

    def __init__(self):
        self.dayDeck = []

    def add_date(self, date_to_day_container, num):
        self.dayDeck.append(DayContainer(date_to_day_container, num))

    def init_num_of_clustering(self, num):
        self.num_of_clustering = num

    def get_list_of_day(self):
        return self.dayDeck

    def clustering(self, x_axis, y_axis):
        first_day = self.dayDeck.pop(x_axis)
        second_day = self.dayDeck.pop(x_axis + y_axis)
        after_clustering = self.cluster_two_day(first_day, second_day)
        after_clustering.modify_date_num(self.num_of_clustering)
        self.num_of_clustering += 1
        self.dayDeck.append(after_clustering)

    @staticmethod
    def cluster_two_day(first_day, second_day):
        if first_day.get_pir_list() is not None:
            pass

        return first_day
        # TODO here
