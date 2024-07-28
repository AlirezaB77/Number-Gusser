
def valid_data(start,end):
    while True:
        try:
            user_input = int(input("Enter Number : "))
            if start <= user_input <= end :
                return user_input
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


