# To-Do List Application

Command-line to-do list app backed by SQLite. Add, remove, edit, and mark tasks as done.

## Setup

```bash
pip install -r requirements.txt
```

## Run

```bash
python3 scripts/run_cli.py
```

## Test

```bash
./run_tests.sh
```

## Structure

```
scripts/run_cli.py   # entry point
src/cli/main.py        # CLI loop
src/cli/model.py        # SQLite-backed task storage
src/cli/view.py         # terminal output (rich)
src/cli/control.py      # ties model/view together
tests/                    # unit tests
db/                       # local SQLite db (gitignored, created at runtime)
docs/app.todo             # task list
CHANGELOG.md
```
