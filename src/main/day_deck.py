from day_container import DayContainer


class DayDeck:
    dayDeck: list

    def __init__(self):
        self.dayDeck = []

    def add_date(self, date_to_day_container):
        self.dayDeck.append(DayContainer(date_to_day_container))

    def get_list_of_day(self):
        return self.dayDeck

    def hierarchical_clustering(self, x_axis, y_axis):
        first_day = self.get_list_of_day().pop(x_axis)
        second_day = self.get_list_of_day().pop(x_axis+y_axis+1)
        after_clustering = self.cluster_two_day(first_day, second_day)
        self.dayDeck.append(after_clustering)


    @staticmethod
    def cluster_two_day(first_day, second_day):
        pass




