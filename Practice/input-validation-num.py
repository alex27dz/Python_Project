while True:
    user_input = input("Enter your age: ")

    # check if it's a number
    if user_input.isdigit():
        age = int(user_input)

        # check valid range
        if 0 < age < 120:
            print("Valid age:", age)
            break
        else:
            print("Age must be between 1 and 119.")

    else:
        print("Please enter a valid number.")