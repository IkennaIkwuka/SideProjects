# Calculator App

CLI calculator that evaluates arithmetic expressions (`+ - * / % ^`), with logic and CLI split into separate modules and tests for the logic layer. Automatically falls back to `Decimal` arithmetic if an expression overflows.

## Run

```bash
python3 -m src.cli.main
```

## Test

```bash
python3 -m pytest tests/
```

## Structure

```
src/cli/main.py         # CLI loop and expression evaluation
src/cli/logic.py         # expression parsing/validation
src/cli/utils/helpers.py # shared helpers
tests/test_logic.py      # tests for the logic layer
docs/                     # requirements notes, todo
```
