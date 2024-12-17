# %%
import utility_operations as ult_ops
import pandas as pd

task_list = []  # Array that holds tasks list.


# Task creation function
def create_tasks():
    max_amount = ult_ops.get_max_task_amount()

    task_amount = ult_ops.ask_task_amount(max_amount)

    while len(task_list) < task_amount:

        if max_amount == 0:
            print(
                "You have exceeded your space for todays task, either update or delete existing tasks"
            )
            break

        task_input = input(
            f"Create a task {len(task_list) + 1}/{task_amount}: "
        ).strip()  # .strip(): Strips input of leading and trailing whitespace.

        if not task_input:  # Checks if "task_input" is empty
            print("Task cannot be empty")
        else:
            task_list.append(task_input)  # Adds "task_input" to tasks list.
            print(f"{len(task_list)}/{task_amount} tasks created successfully.")

    if ult_ops.ask_to_save() == "y":
        ult_ops.save_to_file(task_list)
    else:
        print(f"Your {task_amount} tasks will be deleted when the program ends")


create_tasks()


# %%
# View Tasks function
# def view_tasks():
#     task_view = {"ID": [],"Check", "Tasks": []}
#     for id, task in enumerate(task_list):
#         task_view["ID"].append(id + 1)
#         task_view["Tasks"].append(task)
#     df = pd.DataFrame(task_view)
#     print(df.to_string(index=False))
#     # df


# view_tasks()
# # %%
# # Update Tasks function
# def update_tasks():
#     pass


# %%
