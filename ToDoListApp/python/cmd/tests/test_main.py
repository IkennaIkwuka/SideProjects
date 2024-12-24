index = 0
try:
    with open("python\\docs\\Tasks.txt", "r") as file:
        # print(f"{file.readlines().count("Title:")}")
        fool = file.readlines()
        title = []
        # print(len(file.readlines()))
        for _ in fool:
            # task =_.strip()
            if _.startswith("Title:"):
                title.append(_.strip())
            # task = _.strip()
            # if _.startswith("Title:"):
            #     title.append(_)
            # index +=1
        # print(file.readlines())
        # print(index)
        print(len(title))
        print(title.count("Title:"))
        print(title)
except FileNotFoundError:
    print("File not found")
