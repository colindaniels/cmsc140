def fsum(a, b):
    sm = 0
    for i in range(a, b+1):
        sm += i
    print(sm)
    return sm


def countdown(start, step):
    print('Countdown:')
    for i in range(0, start+1, step):
        print(start - i)


def function_chooser():
    print("Welcome to the function chooser. Please choose a function.")
    print("1 = Cumulative Sum")
    print("2 = Countdown")
    choice = int(input("Your Choice: "))

    print(f"Your choice: {choice}")

    if choice == 1:
        start_number = int(input("Please enter a start number: "))
        end_number = int(input("Please enter an end number: "))
        fsum(start_number, end_number)

    elif choice == 2:
        start_number = int(input("Please enter a start number: "))
        step_number = int(input("Please enter a number to count by: "))
        countdown(start_number, step_number)

function_chooser()