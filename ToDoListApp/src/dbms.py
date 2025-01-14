from shlex import join
import sqlite3
from typing import Any
import traceback
from sqlite3_constants import sqlite3_constraints, sqlite3_datatypes
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
            self.connection.autocommit = False
            self.cursor = self.connection.cursor()
            print("Successful")
        except sqlite3.Error:
            self.get_traceback()

    def close(self):
        try:
            print(f"Closing {self.db_name}.db", end=" ... ")
            self.cursor.close()
            self.connection.close()
            print("Successful")
        except sqlite3.Error:
            self.get_traceback()

    def create(self, table: str, schema: list[tuple[str, str, list[str]]]):
        """Create table for db.

        Args:
            table (str): Name the table.
            schema (str): SQL schema for the table.
        """
        self.validate(schema)

        table_row = []
        for col_name, col_type, col_constraint in schema:
            col_const = " ".join(col_constraint)
            table_row.append(f"{col_name} {col_type} {col_const}")

        _schema = ",\n\t".join(table_row)
        query = f"CREATE TABLE IF NOT EXISTS {table} (\n\t{_schema}\n)"
        try:
            print(f"Executing query: \n{query}")
            self.cursor.execute(query)
            print(f"Table '{table}' has been created")
            self.close()
        except Exception as e:
            print(f"Error: {e}")

    def validate(self, schema: list[tuple[str, str, list[str]]]):
        for col_name, col_type, col_constraint in schema:
            try:
                if col_type not in sqlite3_datatypes:
                    msg = f"Type '{col_type}' is invalid for column '{col_name}'"
                    suggestion = self.sql_type_suggestion(col_type)
                    raise ValueError(f"{msg}\n{suggestion}")

                if col_constraint != "":
                    continue

                for const in col_constraint:
                    if const not in sqlite3_constraints:
                        msg = f"Constraint '{const}' is invalid for column '{col_name}'"
                        suggestion = self.sql_constraint_suggestion(const)
                        raise ValueError(f"{msg}\n{suggestion}")
            except ValueError as e:
                print(f"ERROR: {e}")
                raise

    def sql_type_suggestion(self, col_type: str) -> str:
        suggestions = {"INT": "INTEGER", "REA": "REAL", "TEX": "TEXT", "NUL": "NULL"}
        _ = suggestions.get(col_type[0:3])
        return f"Did you mean '{_}'?" if _ is not None else ""

    def sql_constraint_suggestion(self, col_constraint: str) -> str:
        suggestions = {
            "PRI": "PRIMARY KEY",
            "UNI": "UNIQUE",
            "NOT": "NOT NULL",
            "AUT": "AUTOINCREMENT",
            "FOR": "FOREIGN KEY",
            "REF": "REFERENCES",
            "CHE": "CHECK",
            "DEF": "DEFAULT",
        }
        _ = suggestions.get(col_constraint[0:3])
        return f"Did you mean '{_}'?" if _ is not None else ""

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

    def fetch(
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

        query = f"SELECT * FROM {table}"

        if columns:
            _columns = ",".join(columns)
            query = f"SELECT ({_columns}) FROM {table}"

        if condition:
            query += " " + f"WHERE {condition}"
            self.executing(query, values)
        self.executing(query)
        return self.cursor.fetchall()

    def drop(self, table: str):
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

    def update(
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

    # Utils
    def column_name(self):
        while True:
            if not (user_input := input("Name of column: ")):
                print("ERROR:\nColumn name cannot be empty.\n")
                continue
            if not (user_input.isalpha()):
                print("ERROR:\nMust be alphabetic characters only.\n")
                continue
            break
        return user_input

    def column_type(self, number_of_columns: int, types: list[str]):
        while True:
            if not (
                user_input := input(f"Type of columns {number_of_columns}:").upper()
            ):
                print("ERROR:\nCannot be empty.\n")
                continue
            if user_input not in types:
                print("ERROR:\nNot a valid type.\n")
                continue
            break
        return user_input

    def number_of_columns(self):
        while True:
            try:
                user_input = int(input("How many columns?"))
                if user_input not in (range(9 + 1)):
                    print("ERROR:\nValue too high.\n")
                    continue
            except ValueError:
                print("ERROR:\nMust be a number.\n")
                continue
            break
        print(user_input)


if __name__ == "__main__":
    db_name = "Tasks"
    table_name = "users"
    db = DBMS(db_name.title())
    schema = [
        ("ID", "INTEGER", ["PRIMARY KEY", "AUTOINCREMENT"]),
        ("TASKS", "TEXT", ["UNIQUE", "NOT NULL"]),
        ("USERS", "NULL", [""]),
    ]

    # db.validate(schema)
    db.create(table_name, schema)
    # # print(sqlite3.complete_statement("SELECT foo; "))
    # # db.insert_data("boom", "tasks", ["hi chiwendu"])
    # # db.update_table("users", "tasks = ?", "id = ?", ["nkechi", "4"])
    # # row = db.fetch_table("users")
    # # for _ in row:
    # #     print(_)
    # # db.drop("example")
    # db.close()
