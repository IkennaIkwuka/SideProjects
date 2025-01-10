import sqlite3
import os
from typing import Any
import traceback

os.makedirs("src/", exist_ok=True)


class DBMS:
    def __init__(self, db_name: str) -> None:
        """Connects to Database of name provided. if it does not exists create one.

        Args:
            db_name (str): Database name.
        """
        self.db_name = db_name
        self.connection = sqlite3.connect(f"{db_name}.db")
        self.cursor = self.connection.cursor()

        print(f"Connection to {db_name}.db successfully opened...")

    def close_db(self):
        print(f"Connection to {self.db_name}.db successfully closed...")
        return self.cursor.close()

    def commit(self):
        return self.connection.commit()

    def execute(self, query: str, optional_param=None) -> sqlite3.Cursor:
        """_summary_

        Args:
            query (str): _description_
            optional_param (_type_, optional): _description_. Defaults to None.

        Returns:
            sqlite3.Cursor: _description_
        """
        return (
            self.cursor.execute(query)
            if not optional_param
            else self.cursor.execute(query, optional_param)
        )

    def create_table(self, table_name: str, schema: str):
        """Create table for db.

        Args:
            table_name (str): Name the table.
            schema (str): SQL schema for the table.
        """
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({schema})"

        try:
            print(f"Executing query: {query}")
            self.execute(query)
            print(f"Table: {table_name} has been created")
        except sqlite3.Error:
            self.error_handling()
        self.commit()

    def insert_data(
        self,
        table_name: str,
        columns: tuple[str, ...] = (),
        params: tuple[str, ...] = (),
    ):
        """_summary_

        Args:
            table_name (str): _description_
            columns (tuple[str, ...], optional): _description_. Defaults to ().
            params (tuple[str, ...], optional): _description_. Defaults to ().
        """
        query = f"""
            INSERT INTO {table_name} ({",".join(columns)}) 
            VALUES ({",".join("?" * len(columns))})
            """
        try:
            print(f"Executing query: {query}")
            self.execute(query, params)
            print("Values inserted successfully...")
        except sqlite3.Error:
            self.error_handling()
        self.commit()

    def error_handling(self):
        return traceback.print_exc()

    def fetch_data(
        self,
        table_name: str,
        column_name: tuple[str, ...] = (),
        condition: str | None = None,
        condition_params: tuple[str, ...] = (),
    ):
        """_summary_

        Args:
            table_name (str): Name of the table.
            column_name (tuple[str, ...], optional): _description_. Defaults to ().
            condition (str | None, optional): _description_. Defaults to None.
            condition_params (tuple[str, ...], optional): _description_. Defaults to ().
        """
        if not column_name:
            query = f"SELECT * FROM {table_name} "
        else:
            query = f"SELECT {','.join(column_name)} FROM {table_name} "

        if condition:
            query += f"WHERE {condition} {condition_params}"

        try:
            print(f"Executing query: {query}")
            self.execute(query)
            row = self.cursor.fetchall()
            for _ in row:
                print(_)
        except sqlite3.Error:
            self.error_handling()
        self.commit()

    def drop_table(self, table_name: str):
        query = f"DROP TABLE {table_name}"
        try:
            print(f"Executing query: {query}")
            self.execute(query)
        except sqlite3.Error:
            self.error_handling()
        self.commit()
    
    def update_table(self):
        
        ...


if __name__ == "__main__":
    db = DBMS("Tasks")
    # db.create_table(
    #     "users",
    #     """
    #     id INTEGER PRIMARY KEY AUTOINCREMENT,
    #     tasks TEXT NOT NULL UNIQUE
    #     """,
    # )
    db.insert_data("users", ("tasks",), ("hi chiwendu",))
    db.fetch_data("users", ())
    db.close_db()
