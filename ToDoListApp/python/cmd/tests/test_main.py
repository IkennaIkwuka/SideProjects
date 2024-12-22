tasks = {"title": [], "desc": []}

# title = []
# desc = []
with open("Tasks.txt", "r") as file:
    for _ in file.readlines():
        ff = _.strip()
        if ff.startswith("Title"):
            tasks["title"].append(ff)
        if ff.startswith("Description"):
            tasks["desc"].append(ff)
        # if ff == []:
        #     continue
        # tasks.append(ff)

print(tasks["title"])
print(len(tasks["title"]))
print(tasks["desc"])
print(len(tasks["desc"]))
# print(tasks)
# print(len(tasks))
for index, (t, d) in enumerate(zip(tasks["title"], tasks["desc"]), start=1):
    print(f"\n{index}.\t{t}\n\t{d}")
# print(dir(tasks))
# print(help(tasks))
