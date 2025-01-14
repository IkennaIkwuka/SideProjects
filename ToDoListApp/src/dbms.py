from multiprocessing import Value
from operator import le
import sqlite3
from turtle import st
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
        self.column_names = []
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
        """Create database table

        Args:
            table (str): Table name
            schema (list[tuple[str, str, list[str]]]): List of tuple of str and list[str] to hold the column's name, types and constraints.
        """
        self.validate_create_table(schema)

        table_row = []
        for col_name, col_type, col_constraint in schema:
            col_const = " ".join(col_constraint)
            table_row.append(f"{col_name} {col_type} {col_const}")

        sql = ",\n\t".join(table_row)
        query = f"CREATE TABLE IF NOT EXISTS {table} (\n\t{sql}\n)"
        try:
            print(f"Executing query: \n{query}")
            self.cursor.execute(query)
            print(f"Table '{table}' has been created")
        except Exception as e:
            print(f"Error: {e}")

    def insert_data(self, table: str, schema: list[tuple[list[str], list[str]]]):
        """_summary_

        Args:
            table (str): _description_
            columns (list[str]): _description_
            values (list[str]): _description_
        """
        # for value in values:

        # if column_name not in self.column_names:
        # #     # box.append(column_name)
        # #     # print(len(box))
        # #     # print(box)
        # print(f"column name:{column_name}")
        # print(len(column_name))
        # print(f"columnvalues:{column_values}")
        # print(len(column_values))
        #     # if len(box) != len(column_values):
        #     #     raise ValueError("Not same lenght")
        # col_name.
        # print(len(column_values))

        # column = ",".join(columns)
        # placeholders = ",".join("?" * len(columns))
        # query = f"INSERT INTO {table} ({column}) VALUES ({placeholders})"

        # if self.executing(query, values):
        #     print("Values inserted successfully...")

        # print(len(schema))
        # for _ in schema:
        #     print(f"_:{_}")
        #     for i in _:
        #         print(f"i:{i}")

        # print(len(schema))
        # # box =[]
        self.validate_insert_data(schema)

    def validate_insert_data(self, schema: list[tuple[list[str], list[str]]]):
        columns = []
        values = []
        for column_name, column_values in schema:
            self.validate_insert_column(column_name, column_values)

            for col in column_name:
                self.validate_insert_column_value(column_values, col)
                columns.append(col)

            for val in column_values:
                self.validate_insert_values(val)
                values.append(val)

        return columns, values

    def validate_insert_values(self, val: str):
        if not isinstance(val, str):
            msg = f"Value name '{val}' must be a string"
            raise ValueError(msg)

    def validate_insert_column_value(self, column_values: list[str], col: str):
        if not isinstance(col, str):
            msg = f"Column name '{col}' must be a string"
            raise ValueError(msg)

        if not col.strip():
            _ = ", ".join(column_values)
            msg = f"Column of values '{_}' cannot be empty"
            raise ValueError(msg)

        if not col.isupper():
            msg = f"'{col}' must be in all caps"
            raise ValueError(msg)

        if col not in self.column_names:
            msg = f"'{col}' is not a valid column name"
            raise ValueError(msg)

    def validate_insert_column(self, column_name: list[str], column_values: list[str]):
        if len(column_name) > 1:
            _ = ", ".join(column_name)
            msg = f"Multiple Values '{_}' must only have one value"
            raise ValueError(msg)

        if not column_name:
            _ = ", ".join(column_values)
            msg = f"Column of values '{_}' cannot be empty"
            raise ValueError(msg)

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
    def validate_create_table(self, sql: list[tuple[str, str, list[str]]]):
        for col_name, col_type, col_constraint in sql:
            self.column_names.append(col_name)
            try:
                if col_type not in sqlite3_datatypes:
                    msg = f"Type '{col_type}' is invalid for column '{col_name}'"
                    suggestion = self.sql_type_suggestion(col_type)
                    raise ValueError(f"{msg}\n{suggestion}")

                if not col_constraint:
                    continue

                for col_const in col_constraint:
                    if col_const not in sqlite3_constraints:
                        msg = f"Constraint '{col_const}' is invalid for column '{col_name}'"
                        suggestion = self.sql_constraint_suggestion(col_const)
                        raise ValueError(f"{msg}\n{suggestion}")
            except ValueError as e:
                print(f"ERROR: {e}")
                raise

    def sql_type_suggestion(self, col_type: str) -> str:
        suggestions = {"I": "INTEGER", "R": "REAL", "T": "TEXT", "N": "NULL"}
        _ = suggestions.get(col_type[0])
        return f"Did you mean '{_}'?" if _ is not None else ""

    def sql_constraint_suggestion(self, col_constraint: str) -> str:
        suggestions = {
            "P": "PRIMARY KEY",
            "U": "UNIQUE",
            "N": "NOT NULL",
            "A": "AUTOINCREMENT",
            "F": "FOREIGN KEY",
            "R": "REFERENCES",
            "C": "CHECK",
            "D": "DEFAULT",
        }
        _ = suggestions.get(col_constraint[0])
        return f"Did you mean '{_}'?" if _ is not None else ""

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
        ("USERS", "NULL", []),
    ]
    # db.validate_create_table(schema)
    db.create(table_name, schema)
    # columns = ["tasks", "45"]
    # # print(len(columns))
    # values = ["hi chiwendu"]
    schema = [(["TASKS"], ["hi chiwendu"]), (["USERS"], ["9", "bokk", "4.6"])]
    # print(len(schema))
    db.insert_data("users", schema)
    # # db.update_table("users", "tasks = ?", "id = ?", ["nkechi", "4"])
    # # row = db.fetch_table("users")
    # # for _ in row:
    # #     print(_)
    # # db.drop("example")
    db.close()
