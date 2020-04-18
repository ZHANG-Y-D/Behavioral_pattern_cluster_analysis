from sql_tool import SQLTool
from day_deck import DayDeck

dayDeck = DayDeck()
sqlTool = SQLTool()

value = sqlTool.query_from_sql("select date(t_from) as date from person_position group by date order by date;")


value.pop(0)
value.pop()  # Because the data on the first and last day are not complete, exclude
position_of_date = 1

for date in value:
    dayDeck.add_date(date[0], position_of_date)
    position_of_date += 1

for day_container in dayDeck.get_list_of_day():
    date_curr = day_container.get_date().strftime('%Y-%m-%d')
    result = sqlTool.query_from_sql("select id_room, t_from, t_to from person_position "
                                    "where date(t_from)='" + date_curr + "' or date(t_to)='" + date_curr +
                                    "'order by t_from, t_to, id_room;")
    for tuple_curr in result:
        day_container.add_pir_value(tuple_curr)
