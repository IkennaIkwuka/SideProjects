# %%


TASK_FILE_NAME = "Tasks list.txt"


def get_max_task_amount():
    try:
        with open(TASK_FILE_NAME, "r") as file:
            task_list_file = file.readlines()
            max_amount = 10 - len(task_list_file)
            return max_amount
        if len(task_list_file) > 10:
            print(
                "You have exceeded your space for todays task, either update or delete existing tasks"
            )

    except FileNotFoundError:
        with open(TASK_FILE_NAME, "x") as file:
            print("New file created")
        return 10


# %%
def ask_to_save():
    while True:
        save = input("Would you like to save your tasks?(Y/N): ").lower()

        if not save:
            print("Invalid. Cannot be empty")
        elif save[0] in ["y", "n"]:
            return save
        else:
            print("Invalid input")


# %%
def ask_task_amount(max_amount: int):
    while True:
        # Validate user input and implements error handling.
        try:
            task_amount = int(
                input(
                    f"Hi, You have a maximum of {max_amount} space left for task. How many task would you like to create?: "
                )
            )
            if 1 <= task_amount <= max_amount:
                print(f"You are going to create {task_amount} tasks")
                break
            else:
                print(f"Invalid amount. Input a number between 1 ~ {max_amount}")
        except ValueError:  # Catches and displays ValueError for invalid types.
            print("Invalid input. Input a number")
    return task_amount  # Returns tasks list


# %%
def save_to_file(task_list: list):
    try:
        with open(TASK_FILE_NAME, "a") as file:
            for _ in task_list:
                file.writelines(f"{_}\n")

    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print(f"Unexpected error at {e}")
    else:
        print("File saved successfully")
    finally:
        print("Operation carried out. Here are the tasks")

    #         for i in tasks_list:
    #             print(i)
    # elif save_task[0] != "n":
    #     print("invalid input")
    # else:
    #     for i in tasks_list:
    #         print(i)


# def ask_options():
#     while True:
#         # Validate user input and implements error handling.
#         try:
#             choice = int(input("What do you want to do?: "))

#             if choice not in range(1, 6):  # Checks input in range of 1 ~ 5
#                 print("\nInvalid Input. Input a value from range 1 ~ 5")
#             else:
#                 break
#         # Throw raised error or any unchecked errors
#         except ValueError:  # Catches and displays ValueError for invalid types.
#             print("\nInvalid Input. Input a number")
#     return choice


# def ask_for_index(func_action: str):
#     while True:
#         try:
#             index = int(input(f"What task would you like to {func_action}: ")) - 1
#             return index
#         except ValueError:
#             print("\nInvalid, input number")
