import psycopg2


class SQLTool:
    conn = None
    cur = None

    def __init__(self):
        self.conn = psycopg2.connect("dbname=leozhang user=postgres")
        self.cur = self.conn.cursor()

    def query_from_sql(self, query_string):
        self.cur.execute(query_string)
        return self.cur.fetchall()

    def close_connect(self):
        self.cur.close()
        self.conn.close()
