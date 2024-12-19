task_list = {
    "Title": ["wrtjiwtiwht","w[tok[oeto]]"],
    "Description": ["wtjwtek;tlw"],
}
TITLE = task_list["Title"]
DESCRIPTION = task_list["Description"]

if len(list(zip(TITLE, DESCRIPTION))) == 0:
    print(len(list(zip(TITLE, DESCRIPTION))))
    print("empty ")
elif len(TITLE) != len(DESCRIPTION):
    print(len(list(zip(TITLE, DESCRIPTION))))
    print("Not equal")
else:
    print(len(list(zip(TITLE, DESCRIPTION))))
    print("Not empty")
