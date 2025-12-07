# CHANGELOG

DATE FORMAT -- YEAR-MONTH-DAY -- 2302-12-23

Types of changes

- Added - for new features.
- Changed - for changes in existing functionality.
- Deprecated - for soon-to-be removed features.
- Removed - for now removed features.
- Fixed - for any bug fixes.
- Security - in case of vulnerabilities

## 2025-12-07 - project

### Added

- "python.py" module in SideProjects/utils directory.
- "project_path" function in "python.py" module.

### Changed

- moved "typeWriterEffect" function to "python.py" module.
- improved changelog format.
- refactored file imports in "py_todolistApp" project due to improvement from "project_path" function.
- changed location of changelog.md
- renamed app.todo to todo.md and change its location

### Removed

- removed unnecessary imports/code/comments
- changelog from each project and merged into one changelog.md in "sideProjects" repo
- todo.md from each project and merged it into one in "sideProjects" repo.

## 2025-10-18 - project - py_todolistApp

### Added

- Added functionality to set a limit when trying to add tasks to file and a limit for file size.
- Implemented functionality to check for duplicates when creating a task.
- Added a method with functionality to remove tasks from file.
- Employed the use of indexes.
- Added a functionality to remove all tasks at once.
- Added functionality that saves the current edited task list to file.
- Added a method to edit tasks in file.

### Fixed

- Fixed incorrect imports.
- Resolved path to file issues.

### Changed

- Renamed and changed the functionality of the constructor parameters of the class "ToDoListApp".
- Renamed module "ToDoListApp" to "py_todolist_app".
- Renamed method "update_tasks()" to "edit_tasks()" and improved functionality.
- Restructured order of methods for improved user experience.
- Improved functionality of the core methods streamlining them to reduce cognitive complexity.

### Removed

- Removed methods "load_tasks()", "save_tasks()", "display_tasks()" as well as their functionality as they proved redundant.

## 2025-09-18 - project - py_numberguessingGame

### Added

- Added "Ewo" difficulty.

### Changed

- Streamlined "game_logic()" method's functionality.
- Renamed module to "py_number_guessing_game".

### Removed

- Removed unnecessary/redundant methods.

## 2024-12-16 - project - py_todolistApp

### Added

- Created package of app operations.
- Implemented save tasks functionality in "create_tasks()" function.
- Created "ask_to_save()" and "ask_task_amount()" function in "utility_operations" module.

### Changed

- Refactored "create_tasks()" function to reduce complexity.
- Refactored "task_list" to be a global variable for access across "crud_operations" module.

### Removed

- Removed classes from "crud_operations" and "utility_operations".

## 2024-12-15 - directory - py_todolistApp

### Added

- Added classes to implement Object Oriented Programming (OOP).
- Created modules for "CRUD operations" and "utility operations".
