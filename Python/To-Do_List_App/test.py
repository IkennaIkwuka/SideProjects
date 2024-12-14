# Logic function
def app_logic():

    # Display options
    print("To-Do List App by Ikenna Nicholas Ikwuka")
    print("1. Create tasks")
    print("2. View tasks")
    print("3. Update tasks")
    print("4. Delete tasks")
    print("5. Quit")

    # Loop to take input and catch errors
    while True:
        try:
            choice = int(input("What do you want to do?: "))

            if 1 <= choice <= 5:
                return choice
            else:
                print("Input a value from range 1 ~ 5")
        # Throw raised error or any unchecked errors
        except ValueError:
            print("Input a number")
        except Exception as e:
            print(f"An unexpected error occurred at: {e}")

app_logic()