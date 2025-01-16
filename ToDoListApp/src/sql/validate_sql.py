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


class Validate:
    def __init__(self) -> None:
        self.constraints = [PK, UNIQUE, NOT_NULL, AUTO, FK, REF, CHK, DEF]
        self.datatypes = [INT, TXT, REAL, BLOB, NULL]
        self.valid_columns = []

    def _create(self, schema: list[tuple[str, str, list[str]]]) -> list[str]:
        rows = []
        for col_name, col_type, col_constraint in schema:
            self.valid_columns.append(col_name)

            col_type = col_type.upper()
            col_constraint = [_.upper() for _ in col_constraint]

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

    def _insert(self, schema: list[tuple[list[str], list[str]]]) -> tuple[list[str], list[str]]:
        columns, values = [], []

        self.__parse_insert_param(schema)

        for column_name, column_values in schema:
            for _ in column_name:
                if _.upper() not in self.valid_columns:
                    msg = f"Invalid column name. '{_}'"
                    raise ValueError(msg)
                columns.append(_)

            values.extend(column_values)

        return columns, values

    def __parse_insert_param(self, param: list[tuple[list[str], list[str]]]):
        # Check if the object is a list
        if not isinstance(param, list):
            raise ValueError("Invalid object type. The object must be a list.")

        # Iterate over each element in the list with its index
        for index, item in enumerate(param):
            # Check if each element is a tuple
            if not isinstance(item, tuple) or len(item) != 2:
                msg = f"Invalid object type. Element at index {index} is not a tuple of length 2: {item}"
                raise ValueError(msg)

            # Dynamically validate each tuple's elements using index
            for sub_index, sub_element in enumerate(item):
                if not isinstance(sub_element, list) or not all(
                    isinstance(subitem, str) for subitem in sub_element
                ):
                    msg = f"Invalid object type. Element at index {index} in the tuple (sub-index {sub_index}) must be a list of strings. Found: {sub_element}"
                    raise ValueError(msg)

                self.__parse_insert_missing_value(index, sub_index, sub_element)

    @staticmethod
    def __parse_insert_missing_value(index, sub_index, sub_element):
        # Check if the list is not empty
        if not sub_element:
            msg = f"Missing value. Element at index {index} in the tuple (sub-index {sub_index}) cannot be an empty list."
            raise ValueError(msg)

        # Check if string is empty in list
        for string in sub_element:
            if not string.strip():
                msg = f"Missing value. Element at index {index} in the tuple (sub-index {sub_index}) cannot be an empty string."
                raise ValueError(msg)
