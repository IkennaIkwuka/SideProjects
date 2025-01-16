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


class ValidateOps:
    def __validate_create(self, schema: list[tuple[str, str, list[str]]]):
        rows = [""]
        for col_name, col_type, col_constraint in schema:
            self.__class__.__name__.column_names.append(col_name)

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
