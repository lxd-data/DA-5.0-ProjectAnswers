# name is the variable and it contains a string
name = "Dan"
print("Hello", name)

# distance_in_miles, conversion_rate and distance_kms are all variables that contain numbers
distance_in_miles = 400
conversion_rate = 1.60
distance_in_kms = distance_in_miles * conversion_rate
print("Your trip distance in kilometers is:", distance_in_kms)

# ----- #

my_state = "California"
my_fav_color = "Blue"

# asks for input from user and assigns the response to a variable
your_state = input("What state do you live in? ")
your_fav_color = input("What is your favourite color? ")

print("My code name is", my_state, my_fav_color)
print("Your code name is", your_state, your_fav_color)
print("Let's just keep this between you and I,", your_state, your_fav_color, "!")

# ----- #
my_string ="Python is cool!"

# use the positive index number to access the letter 'c'
letter_c = my_string[10]# <--- write your code here
print(letter_c) 

# use the positive index number to access the second whitespace
white_space = my_string[9] # <--- write your code here
print(white_space) 

# use the positive index number to access the ! symbol
last_char = my_string[14] # <--- write your code here
print(last_char) 

# ----- #

my_string ="Python is cool!"

# use the negative index number to access the letter 'c'
letter_c = my_string[-5] # <--- write your code here
print(letter_c) 

# use the negative index number to access the second whitespace
white_space = my_string[-6] # <--- write your code here
print(white_space)

# use the negative index number to access the letter 'P' 
first_char = my_string[-15] # <--- write your code here
print(first_char) # add the negative index number for the letter 'P' 

# ----- #
data_quote = "The goal is to turn data into information, and information into insight."

quote_length = len(data_quote) # find the length of data_quote
print(quote_length)

last_char =  data_quote[quote_length-1] # use the length of data_quote to access the last character in the string
print(last_char)

# ----- #
savings = 450
deposit = 100
withdrawal = 80


# Write your code below this comment to add a deposit to savings
savings = savings + deposit

print(f"Savings after deposit: {savings}")


# Write your code below this comment to subtract a withdrawal from savings
savings = savings - withdrawal

print(f"Savings after withdrawal: {savings}")

# ----- #
base_a = 10
base_b = 14
height = 5

area = ((base_a + base_b) / 2) * height
print(f"The area of the trapezoid is {area} inches") 