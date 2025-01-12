import sqlite3
from typing import Any
from sqlite3_constants import sql
import traceback
# import os
# os.makedirs("src/", exist_ok=True)


class DBMS:
    def __init__(self, db_name: str) -> None:
        """Connects to Database of name provided. if it does not exists create one.

        Args:
            db_name (str): Database name.
        """

        self.db_name = db_name
        try:
            print(f"Connecting to {db_name}.db", end=" ... ")
            self.connection = sqlite3.connect(f"{db_name}.db")
            self.cursor = self.connection.cursor()
            print("Successful")
        except sqlite3.Error:
            self.get_traceback()

    def close_db(self):
        try:
            print(f"Closing {self.db_name}.db", end=" ... ")
            self.cursor.close()
            self.connection.close()
            print("Successful")
        except sqlite3.Error:
            self.get_traceback()

    def create_table(self, table: str, schema: str):
        """Create table for db.

        Args:
            table (str): Name the table.
            schema (str): SQL schema for the table.
        """
        query = f"CREATE TABLE IF NOT EXISTS {table} ({schema})"
        if self.executing(query):
            print(f"Table '{table}' has been created")

    def insert_data(
        self,
        table: str,
        columns: str | list[str],
        values: list[str],
    ):
        """_summary_

        Args:
            table (str): _description_
            columns (list[str]): _description_
            values (list[str]): _description_
        """

        _columns = ",".join(columns)
        placeholders = ",".join("?" * len(columns))
        query = f"INSERT INTO {table} ({_columns}) VALUES ({placeholders})"

        if self.executing(query, values):
            print("Values inserted successfully...")

    def get_traceback(self):
        print(" Failed\n")
        traceback.print_exc()

    def fetch_table(
        self,
        table: str,
        columns: list[str] | None = None,
        condition: str | None = None,
        values: list[Any] | None = None,
    ) -> list[Any]:
        """_summary_

        Args:
            table (str): _description_
            columns (list[str] | None, optional): _description_. Defaults to None.
            condition (str | None, optional): _description_. Defaults to None.
            values (list[Any] | None, optional): _description_. Defaults to None.

        Returns:
            list[Any]: _description_
        """

        query = f"SELECT * FROM {table} "

        if columns:
            _columns = ",".join(columns)
            query = f"SELECT ({_columns}) FROM {table} "

        if condition:
            query += f"WHERE {condition} "
            self.executing(query, values)
        self.executing(query)
        return self.cursor.fetchall()

    def drop_table(self, table: str):
        query = f"DROP TABLE {table}"
        if self.executing(query):
            print(f"Table '{table}' dropped successfully")

    def executing(self, query: str, params=None) -> bool:
        try:
            print(f"Executing query: {query}", end="... ")
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            print("Successful")
            self.connection.commit()
            print("Transaction committed")
            return True
        except sqlite3.Error:
            self.get_traceback()
            self.connection.rollback()
            print("\nTransaction has been rolled back")
            return False

    def update_table(
        self,
        table_name: str,
        column_to_change: str | list[str],
        condition: str,
        values: list[str],
    ):
        """_summary_

        Args:
            table_name (str): _description_
            column_to_change (str | list[str]): _description_
            condition (str): _description_
            values (tuple[str] | tuple[str, ...]): _description_
        """
        query = f"UPDATE {table_name} SET {column_to_change} WHERE {condition}"
        self.executing(query, values)


if __name__ == "__main__":
    db = DBMS("Tasks")
    # db.create_table(
    #     "boom",
    #     f"""
    #     id {sql.INTEGER} {sql.PRIMARY_KEY},
    #     tasks {sql.TEXT} {sql.NOT_NULL} {sql.UNIQUE}
    #     """,
    # )
    # db.insert_data("boom", "tasks", ["hi chiwendu"])
    # db.update_table("users", "tasks = ?", "id = ?", ["nkechi", "4"])
    # row = db.fetch_table("users")
    # for _ in row:
    #     print(_)
    db.drop_table("example")
    db.close_db()
