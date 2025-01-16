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


class Valid:
    def __init__(self) -> None:
        self.constraints = [PK, UNIQUE, NOT_NULL, AUTO, FK, REF, CHK, DEF]
        self.datatypes = [INT, TXT, REAL, BLOB, NULL]
        self.valid_columns = []

    def _create(self, schema: list[tuple[str, str, list[str]]]):
        rows = [""]
        for col_name, col_type, col_constraint in schema:
            self.valid_columns.append(col_name)

            if col_type not in self.datatypes:
                msg = f"Type '{col_type}' is invalid for column '{col_name}'"
                suggestion = self.__type_suggestion(col_type)
                raise ValueError(f"{msg}\n{suggestion}")

            if not col_constraint:
                continue

            for col_const in col_constraint:
                if col_const not in self.constraints:
                    msg = f"Constraint '{col_const}' is invalid for column '{col_name}'"
                    suggestion = self.__constraint_suggestion(col_const)
                    raise ValueError(f"{msg}\n{suggestion}")

            col_const = " ".join(col_constraint)
            rows.append(f"{col_name} {col_type} {col_const}")
        return [_ for _ in rows if _.strip()]

    @staticmethod
    def __type_suggestion(col_type: str) -> str:
        suggestions = {"I": INT, "R": REAL, "T": TXT, "N": NULL}
        _ = suggestions.get(col_type[0])
        return f"Did you mean '{_}'?" if _ is not None else ""

    @staticmethod
    def __constraint_suggestion(col_constraint: str) -> str:
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

    def _insert(self, schema: list[tuple[list[str], list[str]]]):
        columns, values = [""], [""]

        for column_name, column_values in schema:
            col_name = ", ".join(column_name)
            col_val = ", ".join(column_values)

            # if not isinstance(column_name, list) or not isinstance(column_values, list):
            #     msg = "sus"
            #     raise ValueError(msg)

            if len(column_name) != 1 or len(column_values) != 1:
                msg = f"Size mismatch expected 1 value\nColumn name: '{col_name}'\nColumn value: '{col_val}'"
                raise ValueError(msg)

            if not column_name or not column_values:
                msg = f"Cannot be empty\nColumn name: '{col_name}'\nColumn value: '{col_val}'"
                raise ValueError(msg)

            for col in column_name:
                self.__insert_columns(column_values, col, self.valid_columns)
                columns.append(col)

            for val in column_values:
                self.__insert_values(val, column_name)
                values.append(val)

        # Remove empty string '{""}'
        column = [_ for _ in columns if _.strip()]
        value = [_ for _ in values if _.strip()]

        return column, value

    @staticmethod
    def __insert_columns(column_values: list[str], col: str, column_names: list[str]):
        if not isinstance(col, str):
            msg = f"Column name '{col}' must be a string"
            raise ValueError(msg)

        if not col.strip():
            _ = ", ".join(column_values)
            msg = f"Column of values '{_}' cannot be empty"
            raise ValueError(msg)

        if col.upper() not in column_names:
            msg = f"'{col}' is not a valid column name"
            raise ValueError(msg)

    @staticmethod
    def __insert_values(val: str, column_name: list[str]):
        if not isinstance(val, str):
            msg = f"Value name '{val}' must be a string"
            raise ValueError(msg)

        if not val.strip():
            _ = ", ".join(column_name)
            msg = f"Column '{_}' cannot be empty"
            raise ValueError(msg)
