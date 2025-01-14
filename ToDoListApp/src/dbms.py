import sqlite3
from sre_constants import IN
from typing import Any
import traceback
# import os
# os.makedirs("src/", exist_ok=True)

# Constraints
PK = "PRIMARY KEY"
UNIQUE = "UNIQUE"
NOT_NULL = "NOT NULL"
AUTO = "AUTOINCREMENT"
FK = "FOREIGN KEY"
REF = "REFERENCES"
CHK = "CHECK"
DEF = "DEFAULT"

# Datatype
INT = "INTEGER"
TXT = "TEXT"
REAL = "REAL"
BLOB = "BLOB"
NULL = "NULL"


class DBMS:
    def __init__(self, db_name: str) -> None:
        """Connects to Database of name provided. if it does not exists create one.

        Args:
            db_name (str): Database name.
        """

        self.constraints = [PK, UNIQUE, NOT_NULL, AUTO, FK, REF, CHK, DEF]
        self.datatypes = [INT, TXT, REAL, BLOB, NULL]

        self.column_names = []
        try:
            print(f"Connecting to {db_name}.db", end=" ... ")
            self.connection = sqlite3.connect(f"{db_name}.db")
            self.connection.autocommit = False
            self.cursor = self.connection.cursor()
            print("Successful")
        except sqlite3.Error:
            traceback.print_exc()

    def commit(self):
        print("Transaction committed")
        return self.connection.commit()

    def rollback(self):
        print("Transaction rollback")
        return self.connection.rollback()

    def close(self, db_name):
        print(f"Closing {db_name}.db", end=" ... ")
        self.cursor.close()
        self.connection.close()
        print("Successful")

    def create(self, table: str, schema: list[tuple[str, str, list[str]]]):
        """Create database table

        Args:
            table (str): Table name
            schema (list[tuple[str, str, list[str]]]): List of tuple of str and list[str] to hold the column's name, types and constraints.
        """

        table_row = self.validate_create(schema)

        sql = ",\n\t".join(table_row)
        query = f"CREATE TABLE IF NOT EXISTS {table} (\n\t{sql}\n)"
        try:
            print(f"\nExecuting query: \n{query}")
            self.cursor.execute(query)
            print(f"Table '{table}' has been created")
            self.commit()
        except Exception as e:
            print(f"Unexpected Error: {e}")
            self.rollback()

    # Utils
    def validate_create(self, schema: list[tuple[str, str, list[str]]]):
        rows = [""]
        for col_name, col_type, col_constraint in schema:
            self.column_names.append(col_name)

            if col_type not in self.datatypes:
                msg = f"Type '{col_type}' is invalid for column '{col_name}'"
                suggestion = self.type_suggestion(col_type)
                raise ValueError(f"{msg}\n{suggestion}")

            if not col_constraint:
                continue

            for col_const in col_constraint:
                if col_const not in self.constraints:
                    msg = f"Constraint '{col_const}' is invalid for column '{col_name}'"
                    suggestion = self.constraint_suggestion(col_const)
                    raise ValueError(f"{msg}\n{suggestion}")

            col_const = " ".join(col_constraint)
            rows.append(f"{col_name} {col_type} {col_const}")
        return [_ for _ in rows if _.strip()]

    # Utils
    def type_suggestion(self, col_type: str) -> str:
        suggestions = {"I": INT, "R": REAL, "T": TXT, "N": NULL}
        _ = suggestions.get(col_type[0])
        return f"Did you mean '{_}'?" if _ is not None else ""

    # Utils
    def constraint_suggestion(self, col_constraint: str) -> str:
        suggestions = {
            "P": PK,
            "U": UNIQUE,
            "N": NOT_NULL,
            "A": AUTO,
            "F": FK,
            "R": REF,
            "C": CHK,
            "D": DEF,
        }
        _ = suggestions.get(col_constraint[0])
        return f"Did you mean '{_}'?" if _ is not None else ""

    def insert(self, table: str, schema: list[tuple[list[str], list[str]]]):
        """_summary_

        Args:
            table (str): _description_
            columns (list[str]): _description_
            values (list[str]): _description_
        """
        columns, values = self.validate_insert(schema)
        col = ", ".join(columns)
        val = ", ".join("?" * len(values))
        query = f"INSERT INTO {table} ({col}) VALUES ({val})"
        try:
            print(f"\nExecuting query: \n{query}")
            self.cursor.execute(query, values)
            print(f"Values: '{', '.join(values)}' inserted into table '{table}'")
            self.commit()
        except Exception as e:
            print(f"Unexpected Error: {e}")
            self.rollback()

    # Utils
    def validate_insert(self, schema: list[tuple[list[str], list[str]]]):
        columns = [""]
        values = [""]
        for column_name, column_values in schema:
            col_name = ", ".join(column_name)
            col_val = ", ".join(column_values)
            if len(column_name) > 1:
                msg = f"Multiple Columns '{col_name}' must only have one value"
                raise ValueError(msg)

            if not column_name:
                col_name = ", ".join(column_values)
                msg = f"Column of values '{col_name}' cannot be empty"
                raise ValueError(msg)

            if len(column_values) > 1:
                msg = f"Multiple Values '{col_val}' must only have one value"
                raise ValueError(msg)

            if not column_values:
                col_val = ", ".join(column_name)
                msg = f"Values of column '{col_val}' cannot be empty"
                raise ValueError(msg)

            for col in column_name:
                self.validate_insert_columns(column_values, col)
                columns.append(col)

            for val in column_values:
                self.validate_insert_values(val, column_name)
                values.append(val)
        # Remove empty string '{""}'
        column = [_ for _ in columns if _.strip()]
        value = [_ for _ in values if _.strip()]

        return column, value

    # Utils
    def validate_insert_values(self, val: str, column_name: list[str]):
        if not isinstance(val, str):
            msg = f"Value name '{val}' must be a string"
            raise ValueError(msg)
        if not val.strip():
            _ = ", ".join(column_name)
            msg = f"Column of values '{_}' cannot be empty"
            raise ValueError(msg)

    # Utils
    def validate_insert_columns(self, column_values: list[str], col: str):
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

    def fetch(
        self,
        table: str,
        columns: list[str] | None = None,
        condition: str | None = None,
        values: list[str] | None = None,
    ):
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
            self.validate_fetch_column(columns)
            column = ", ".join(columns)
            query = f"SELECT {column} FROM {table}"

        if condition:
            ...

        try:
            print(f"\nExecuting query: \n{query}")
            self.cursor.execute(query)
            print("Viewed successful")
            self.commit()
        except Exception as e:
            print(f"Unexpected Error: {e}")
            self.rollback()

        row = self.cursor.fetchall()
        for _ in row:
            print(_)

    def validate_fetch_column(self, columns):
        for col in columns:
            if not isinstance(col, str):
                msg = f"'{col}' must be a string."
                raise ValueError(msg)
            if (not col) or (not col.strip()):
                msg = "Cannot be empty"
                raise ValueError(msg)
            if not col.isupper():
                msg = f"'{col}' must be in all caps"
                raise ValueError(msg)
            if col not in self.column_names:
                msg = f"'{col}' is not a valid column"
                raise ValueError(msg)

        # if columns:
        #     _columns = ",".join(columns)
        #     query = f"SELECT ({_columns}) FROM {table}"

        # if condition:
        #     query += " " + f"WHERE {condition}"
        #     self.executing(query, values)
        # self.executing(query)
        # return self.cursor.fetchall()

    # def update(
    #     self,
    #     table_name: str,
    #     column_to_change: str | list[str],
    #     condition: str,
    #     values: list[str],
    # ):
    #     """_summary_

    #     Args:
    #         table_name (str): _description_
    #         column_to_change (str | list[str]): _description_
    #         condition (str): _description_
    #         values (tuple[str] | tuple[str, ...]): _description_
    #     """
    #     query = f"UPDATE {table_name} SET {column_to_change} WHERE {condition}"
    #     self.executing(query, values)

    def drop(self, table: str):
        query = f"DROP TABLE IF EXISTS {table}"
        try:
            self.cursor.execute(query)
            print(f"Table '{table}' dropped successfully")
        except Exception as e:
            print(f"Unexpected Error: {e}")

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
    db_name = "Main"
    table = "MASTER"
    db = DBMS(db_name.title())

    schema = [
        ("ID", INT, [PK, AUTO]),
        ("TASKS", TXT, [UNIQUE, NOT_NULL]),
        ("USERS", TXT, [UNIQUE]),
    ]
    db.create(table, schema)

    # schema = [(["TASKS"], ["hi ogonna"]), (["USERS"], ["28"])]
    # db.insert(table, schema)
    column = ["TASKS", "USERS"]
    condition = [
        (
            "ID = ?",
            "j",
        ),
        ("2", "3", "k"),
    ]

    db.fetch(table, column)

    # db.drop("example")
    db.close(db_name)
