from day_container import DayContainer


class DayDeck:
    dayDeck: list

    def __init__(self):
        self.dayDeck = []

    def add_date(self, date_to_day_container, num):
        self.dayDeck.append(DayContainer(date_to_day_container, num))

    def get_list_of_day(self):
        return self.dayDeck
