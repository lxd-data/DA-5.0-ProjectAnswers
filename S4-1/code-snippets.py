print("Some Data")

cube = pow(2, 3)
num1 = 2
num2 = 3

cube = pow(num1, num2)
cube = pow(3,1)
cube = pow(cube,3)

my_to_do_list = ["Wash car", "do homework", "make dinner", "clean bathroom"]
my_to_do_list = ["Wash car", "do homework", "make dinner", "clean bathroom"]

count = 0
for chore in my_to_do_list:
    count = count + 1

print(count)

my_to_do_list = ["Wash car", "do homework", "make dinner", "clean bathroom"]
your_to_do_list = ["Mow the lawn", "do homework", "clean kitchen"]

my_to_do_list = ["Wash car", "do homework", "make dinner", "clean bathroom"]
your_to_do_list = ["Mow the lawn", "do homework", "clean kitchen"]

count1 = 0
for chore in my_to_do_list:
    count1 = count1 + 1

count2 = 0
for chore in your_to_do_list:
    count2 = count2 + 1

print(f"I have {count1} chores and you have {count2}")

print(f"I have {len(my_to_do_list)} chores and you have {len(your_to_do_list)}")

# example function that adds two numbers together
def add(num1, num2):
    sum = num1 + num2
    print(f"The sum of the numbers is: {sum}")
    return sum


add(5,3)
def say_name():
    print("My name is _")

hello = "Hello There"

def say_hello():
    print(f"Why {hello}.")

def substring(word, length):
    sub = ""
    for i in range(length):
        sub = sub + word[i]
    print(sub)


def resolve_roll(die1, die2):
    roll = die1 + die2
    if roll == 12:
        return "critical hit"
    elif roll > 3:
        return "hit"
    elif roll == 3:
        return "miss"
    else: 
        return "critical miss"

print(resolve_roll(1,1))

def say_full_name(f_name, l_name):
    return f"My name is {f_name} {l_name}"

phrase = say_full_name("Mike", "Johnson")

if "Mike" in phrase:
    print(phrase)
else:
    print("I thought your name was Mike")

def compute_pay(rate, hours):
    return(f"Hours: {hours} | Rate: {rate} | Pay: ${rate * hours}")

print(compute_pay(25, 40))

def compute_pay(rate, hours):
      return(f"Hours: {hours} | Rate: {rate} | Pay: ${rate * hours}")

print(compute_pay(rate=25, hours=35))

def compute_pay(rate, hours):
    return(f"Hours: {hours} | Rate: {rate} | Pay: ${rate * hours}")

employee_hours = 40
employee_rate = 25
print(compute_pay(rate=employee_rate, hours=employee_hours))
print(compute_pay(hours=employee_hours, rate=employee_rate))

def compute_pay(rate, hours=40):
      return f"${hours * rate}"

print(compute_pay(rate=25))
def compute_pay(rate, hours=40):
      return f"${hours * rate}"

print(compute_pay(rate=25, hours=25))

def compute_pay(rate, hours=40, overtime=0):
    if overtime == 0:
        return(f"Hours: {hours} | Rate: {rate} | Pay: ${rate * hours}")
    else: 
        pay = (rate * hours) + ((rate * 1.5) * overtime)
        return(f"Hours: {hours} | Rate: {rate} | Pay: ${pay}")

print(compute_pay(25))
print(compute_pay(25, overtime=10))
pow(38, -1, mod=97)


greeting = "Hello"

def greet(name):
    return f"{greeting}, {name}!"

print(greet("Isaiah"))


def cube(num):
    result = num ** 2
    return result

cube(10)

def cube(num):
    result = num ** 2
    return result

cube(10)

num = 10

def cube():
    num = 5
    result = num ** 2
    return result

print(num)
cube()

outer_list = [1,2,3] # define a global list
print(outer_list) 

def change_list(inner_list): 
     inner_list[0] = 2   # this will change the outer_list
 
change_list(outer_list)     
print(outer_list)  

def add(a, b):
    return a + b

def multiply(num1, num2):
    """Takes two integers, num1 and num2, and returns them multiplied together."""
    return num1*num2

def find_max(data):
    """Takes an iterable of integers, data, as input and returns the max item, an integer."""
    max = 0
    for num in data:
        if num > max:
            max = num
    return max

def find_max(data):
    '''Takes an iterable of integers, data, as input and returns the max item, an integer.'''
    max = 0
    for num in data:
        if num > max:
            max = num
    return max

def reverse_string(str1):
    '''Takes a string, str1, as input, reverses it, and returns the reversed string.'''
    reverse_str1 = ''
    i = len(str1)
    while i > 0: 
        reverse_str1 += str1[i - 1] # add the last character in str1 to reverse_str1
        i -= 1 # decrement by 1
    return reverse_str1

def reverse_string(str1):
    '''Takes a string, str1, as input, reverses it, and returns the reversed string.'''
    reverse_str1 = ''
    i = len(str1)
    while i > 0: 
        reverse_str1 += str1[i - 1] # add the last character in str1 to reverse_str1
        i -= 1 # decrement by 1
    return reverse_str1

def find_max(data):
    '''Takes an iterable of integers, data, as input and returns the max item, an integer.'''
    max = 0
    for num in data:
        if num > max:
            max = num
    return max

def multiply(num1, num2):
    '''Takes two integers, num1 and num2, and returns them multiplied together.'''
    return num1*num2

def square(a):
    '''The argument, a, is squared and returned
    '''
    return a**a

def square(a):
    '''Takes an integer or float, a, as input, squares it, and returns it as a float or integer.'''
    return a**a

def multiply(a, b):
    """Takes in two integers, a and b, and returns their product, an integer."""
    return a*b

def find_emp(col_name, name):
    names = employees[col_name]
    if name in names:
        i = names.index(name)
        return f"{employees['fnames'][i]} {employees['lnames'][i]}"
    else:
        return "Name not found"

def find_emp(col_name, name):
    """ 
    Checks if the name of an employee exists. 
  
    find_emp takes col_name, a column name, and name,
    the name of an employee, as inputs, searches for 
    the specified name in the specified column, and returns
    the first name and last name or 'Name not found'.
  
    Arguments: 
    col_name (str): the column name to search.
    name (str) : the name to search for.
  
    Returns: 
    str: Either the employees name or "Name not found."
    """
    names = employees[col_name]
    if name in names:
        i = names.index(name)
        return f"{employees['fnames'][i]} {employees['lnames'][i]}"
    else:
        return "Name not found"

def find_emp(col_name, name):
    """ 
    Checks if the name of an employee exists. 
  
    find_emp takes col_name, a column name, and name,
    the name of an employee, as inputs, searches for 
    the specified name in the specified column, and returns
    the first name and last name or 'Name not found'.
  
    Parameters
    ==========
    col_name (str): the column name to search.
    name (str) : the name to search for.
  
    Returns
    ==========
    str: Either the employees name or "Name not found."

    Examples
    ==========
    >>> find_emp("Full Name", "Dan Murphy")
    Dan Murphy
    >>> fund_emp("Employee_ID", "Dan Murphy")
    Name not found
    """
    names = employees[col_name]
    if name in names:
        i = names.index(name)
        return f"{employees['fnames'][i]} {employees['lnames'][i]}"
    else:
        return "Name not found"

def find_emp(col_name, name):
    """ 
    Checks if the name of an employee exists. 
  
    find_emp takes col_name, a column name, and name,
    the name of an employee, as inputs, searches for 
    the specified name in the specified column, and returns
    the first name and last name or 'Name not found'.
  
    Args
    ==========
    col_name (str): the column name to search.
    name (str) : the name to search for.
  
    Returns
    ==========
    str: Either the employees name or "Name not found."

    """
    names = employees[col_name]
    if name in names:
        i = names.index(name)
        return f"{employees['fnames'][i]} {employees['lnames'][i]}"
    else:
        return "Name not found"

def find_emp(col_name, name):
    """ 
    Checks if the name of an employee exists. 
  
    find_emp takes col_name, a column name, and name,
    the name of an employee, as inputs, searches for 
    the specified name in the specified column, and returns
    the first name and last name or 'Name not found'.
  
    Parameters
    ----------
    col_name : (str)
             the column name to search.
    name : (str)
             the name to search for.
  
    Returns
    ----------
    str 
             Either the employees name or "Name not found."
    """
    names = employees[col_name]
    if name in names:
        i = names.index(name)
        return f"{employees['fnames'][i]} {employees['lnames'][i]}"
    else:
        return "Name not found"


def minutesToSeconds(minutes):
    """
    Converts the number of minutes to seconds
    """
    return minutes*60

def minutesToSeconds(minutes):
    """Accepts an integer, minutes, as input, converts it to seconds, and returns an integer."""
    return minutes*60

def findMin(data):
    min = data[0] # set min to arbitrary number at first index
    for num in data[1:]:
        if num < min:
            min = num
    return min

def maxDifference():
    i = 0
    j = 1
    differences = []
    while j < len(data):
        diff = data[j] - data[i]
        differences.append(diff)
        # increment each value
        i += 1
        j += 1
    return max(differences)

def findMax(data):
    max = data[0] # set max to arbitrary number at index 0
    for num in data[1:]:
        if num > max:
            max = num
    return max

def maxDifference(data):
    i = 0
    j = 1
    differences = []
    while j < len(data):
        diff = data[j] - data[i]
        differences.append(diff)
        # increment each value
        i += 1
        j += 1
    return max(differences)