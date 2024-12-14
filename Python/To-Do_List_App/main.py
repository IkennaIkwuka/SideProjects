# while len(tasks_list) < 11:

#     save_task = input("Would you like to save your tasks? (y/n)").lower().strip()
#     if save_task[0] == "y":
#         try:
#             with open("Task.txt", "r") as file:
#                 if len(file.readlines()) >= 10:
#                     print("The file is full")
#         except FileNotFoundError:
#             with open("Task.txt", "a") as file:
#                 file.writelines(tasks_list)
#         except Exception as e:
#             print(f"Unexpected error at {e}")
#         else:
#             print("File saved successfully")
#         finally:
#             print("Operation carried out. Here are the tasks")
#             for i in tasks_list:
#                 print(i)
#     elif save_task[0] != "n":
#         print("invalid input")
#     else:
#         for i in tasks_list:
#             print(i)
#         break
