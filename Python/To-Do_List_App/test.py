try:
    choice = int(input("Hi: "))
    # if not choice.
    #     raise Exception("hiiiii")
except ValueError:
    print("value hi")
except Exception as e:
    print(f"error at {e}")