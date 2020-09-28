import calculator 


def get_calculation():
    user_calculation = ""
    while user_calculation not in ["add", "subtract", "multiply", "divide"]:
        user_calculation = input("what calculation would you like to perform: add, subtract, multiply or divide?").strip().lower()
    return user_calculation


def get_numbers():
    user_numbers = []
    while len(user_numbers) != 2:
        user_numbers = input("Enter two comma-separated numbers:").replace(",", " ").split()
    return user_numbers

def main():
    calculation = get_calculation()
    numbers = get_numbers()
    response = calculator.calculate( calculation,numbers )
    print(response)

# Do not delete
if __name__ == '__main__':
    print(main())
