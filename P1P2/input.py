import library 

def get_numbers():
    """
    Asks a user to input a list of comma separated numbers and returns a list
    """
    num_list = []
    while len(num_list) <= 0:
        user_input = input("Enter a list of numbers separated by commas: ")
        remove_commas = user_input.replace(",", " ")
        num_list = [int(char) for char in remove_commas if char.isnumeric()]
    return num_list

def get_operation():
    """
    Ask a user to input a statistical operation and returns a string
    """
    operation = ""
    while operation not in ["mean", "median", "std dev", "all"]:
        operation = input("What statistic would you like to know? Please enter mean, median, std dev or all: ").lower()
    return operation

def get_input():
  """
  Takes user input and returns the result of a stastical operation 
  """
  data = get_numbers()
  operation = get_operation()
  result = library.report(operation, data)
  return result


# IMPORTANT: DO NOT DELETE!
if __name__ == '__main__':
    print(get_input())