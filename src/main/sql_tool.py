import sys
import psycopg2


class SQLTool:
    conn = None
    cur = None

    def __init__(self):
        pass

    def connection_sql(self, dbname, user, password=None, host=None, port=None):
        try:
            self.conn = psycopg2.connect("dbname=" + dbname + " user=" + user + " password=" +
                                         password + " host=" + host + " port=" + port)
        except psycopg2.Error as e:
            print("\033[1;31m Connection database error. \033[0m " + str(e))
            print("\033[1;31m Program EXIT, please check the database problem and reopen it, think you! \033[0m ")
            sys.exit()
        self.cur = self.conn.cursor()

    def query_from_sql(self, query_string):
        try:
            self.cur.execute(query_string)
            return self.cur.fetchall()
        except psycopg2.Error as e:
            print("\033[1;31m Your dataset may have some problem, "
                  "Please check the dataset according to the documentation. \033[0m ")
            print("Problem: " + str(e))
            print("\033[1;31m Program EXIT. \033[0m ")
            self.close_connect()
            sys.exit()

    def close_connect(self):
        try:
            self.cur.close()
            self.conn.close()
        except psycopg2.Error:
            pass
