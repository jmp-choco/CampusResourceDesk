def get_number(message):
    while True:
        try:
            number = int(input(message))

            if number > 0:
                return number
            else:
                print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")