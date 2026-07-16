import psycopg2
from psycopg2 import sql

from config import DB_CONFIG


class Database:

    def __init__(self):
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = psycopg2.connect(**DB_CONFIG)
        self.cursor = self.connection.cursor()

        print("✓ Connected to PostgreSQL")

    def execute_script(self, script: str):
        """
        Executes an entire SQL script.

        If the last SQL statement returns rows,
        return both the column names and data.
        """

        statements = [
            s.strip()
            for s in script.split(";")
            if s.strip()
        ]

        rows = []
        columns = []

        for statement in statements:

            self.cursor.execute(statement)

            if self.cursor.description:
                columns = [
                    column[0]
                    for column in self.cursor.description
                ]

                rows = self.cursor.fetchall()

        self.connection.commit()

        return columns, rows

    def close(self):

        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        print("✓ Connection Closed")