import psycopg2

class ProspectDatabase:

    def __init__(self, user, password, dbname = "prospects")
        self.user = user
        self.password = password
        self.dbname = dbname
        self.conn = None
        self.cursor = None
        self.create_connection()

    def create_connection(self):
        try:
            self.conn = psycopg2.connect(
                database = self.dbname,
                user = self.user,
                password = self.password
            )

            self.cursor = self.conn.cursor()
        except Error as e:
            print(error)

    def clear_table(table):
        pass
