# %%
import utility_operations as ult_ops

task_list = []  # Array that holds tasks list.

# %%
# Task creation function
def create_tasks():
    
    task_amount = ult_ops.ask_task_amount()

    while len(task_list) < task_amount:

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

    return task_list 


# %%
# View Tasks function
def view_tasks():
    
    
# # %%
# # Update Tasks function
# def update_tasks():
#     pass


# %%
