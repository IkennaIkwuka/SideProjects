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
def ask_task_amount():
    while True:
        # Validate user input and implements error handling.
        try:
            task_amount = int(
                input("Hi!, how many task would you like to create?(maximum of 10): ")
            )
            if 1 <= task_amount <= 10:
                print(f"You are going to create {task_amount} tasks")
                break
            else:
                print("Invalid amount. Input a number between 1 ~ 10")
        except ValueError:  # Catches and displays ValueError for invalid types.
            print("Invalid input. Input a number")
    return task_amount  # Returns tasks list


# %%
def save_to_file(task_list: list):

    try:
        with open("Task.txt", "r") as file:
            if len(file.readlines()) >= 10:
                print("The file is full")
    except FileNotFoundError:
        with open("Task.txt", "a") as file:
            file.writelines(task_list)
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


