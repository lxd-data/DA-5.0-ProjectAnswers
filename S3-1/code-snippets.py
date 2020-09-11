exchange_rate = 1.31
exchange_rate = 1.31
usd_to_cad = 5.25 * 1.31
usd_to_cad = 5.25 * exchange_rate
greeting = "Hello World"
print(greeting)
name = "Anisa"
print("Hello", name)
name = "Anisa" # assign name to be Anisa
name = "Jose" # reassigned name to be Jose
print("Hello", name)
item_count = item_sum = 0
print(item_count)
print(item_sum)
item_count, item_sum, item_name = 5, 10, "cell phone"
print(item_count)
print(item_sum)
print(item_name)
print("Your trip distance in kilometers is:", 381.9*1.60)

# bad variable names
x = 72
x_f = 72

# better, but still not good variable names
temp = 72
temp_f = 72

# good variable names
temp_fahrenheit = 72
temp_in_fahrenheit = 72
temp_fahr = 72

min_val = 50 # minimum value
max_val = 600 # maximum value
avg_val = 325 # average value
std_val = 165.83123951777 # standard deviation
# using x and y
x = 163.6
y = 60

# using descriptive names
trip_distance = 163.6
avg_speed = 60

# printing an integer directly
print(30)
30

# declaring a variable and assigning it an integer value
my_int = 30
print(my_int)
math_add = 5.5 + 5
print(type(math_add))
year = 2017

print("We made the most sales in :" + str(year))

my_string = "Python is cool!"
my_string[0] # accessing the first character in the string

my_string[6] # accessing the first white space in the string

my_string[4] # accessing the fifth character in the string

letter_c = my_string[10] # uses the positive index number to access the letter 'c'
print(letter_c)
white_space = my_string[9] # uses the positive index number to access the second whitespace
print(white_space)
last_char = my_string[14] # uses the positive index number to access the last character
print(last_char)

my_string = "Python is cool!"
print(my_string[-1])
print(my_string[-10])
print(my_string[-3])
letter_c = my_string[-5] # uses the negative index number to access the letter 'c'
print(letter_c)

white_space = my_string[-6] # uses the negative index number to access the second whitespace
print(white_space)

first_char = my_string[-15] # uses the negative index number to access the first character
print(first_char)

long_string = "The first step in the data analysis process is defining the questions you want to ask."
print(len(long_string))

long_string = "The first step in the data analysis process is defining the questions you want to ask."
print(long_string[len(long_string)- 1])
long_string = "The first step in the data analysis process is defining the questions you want to ask."
print(long_string[len(long_string)- 1])
print(long_string[-1])
print(len("12$ 4"))

find_last = "Find the last element of this string"

spider_guy = "Peter Parker!"
print(spider_guy[6:12])
print(spider_guy[-7:-3])

spider_guy = "Peter Parker!"
print(spider_guy[:5])
print(spider_guy[6:])

string = '0123456789'
evens = string[2:9:2] # starts at index 2, ends and exludes index 9, with a stride of 2
print(evens)

string = '0123456789'
evens = string[2::2] # starts at index 2, goes to the end of the string, with a stride of 2
print(evens)


string = '0123456789'
print(string[::2]) # every other character in the entire string
print(string[:9:3]) # every 3rd character from the beginning of the string until but not including index 9
print(string[1:10:2]) # start at index 1, end at index 10, every 2 characters


temp = 70

# individual values
print("It is", temp, "degrees fahrenheit today")

# concatenation
print("It is " + str(temp) + " degrees fahrenheit today")


first_word = "Hello"
second_word = "World"
print(first_word + second_word)
first_word = "Hello"
second_word = "World"
print(first_word + " " + second_word)

print("This is an {} of {} arguments".format("example", "default"))
print("This is an {0} of {1} arguments".format("example", "positional"))
print("This is an {word_one} of {word_two} arguments".format(word_one ="example", word_two = "keyword"))

# values as variables
mean = 8
median = 15

# passing variables to format()
print("The mean is {} and the median is {}".format(mean, median))

# variables
mean = 8
median = 15
print(f'The mean is {mean} and the median is {median}')
'The mean is 8 the median is 15'

# equation
length = 5
width = 10
print(f'The area of the rectangle is {length * width}')


# Product
calculation = "product"
num_one = 8
num_two = 15
print("The {} of {} and {} is {}".format(calculation, num_one, num_two, num_one * num_two))
print(f"The {calculation} of {num_one} and {num_two} is {num_one * num_two}")

# Sum
calculation = "sum"
print("The {} of {} and {} is {}".format(calculation, num_one, num_two, num_one + num_two))
print(f"The {calculation} of {num_one} and {num_two} is {num_one + num_two}")
print("Python".replace("Py", "Mara"))

column_name = 'sale price (dollars)'
column_name_replace = column_name.replace(" ", "_")
print(column_name_replace)

org_column_name = " Sale Price (Dollars) "
new_column_name = org_column_name.strip().lower().replace(' ', '_').replace('(', '').replace(')', '')
print(new_column_name)

string_date = "08 19 2020"
new_date = string_date.replace(" ", "-")
print(new_date)

# example 1: adding and subtracting integers directly
print(8 + 7)

print(8 - 7)

# example 2: adding  and subtracting two float variables
float_one = 42.25
float_two = 10.50
print(float_one + float_two)

print(float_one - float_two)


# example 3: adding and subtracting floats and integers
flt = 10.50
num = 15
print(num + flt)

print(num - flt)


# example 1: multiplying and dividing two integers directly
print(50 / 5)
print(50 * 5)

# example 2 : multiplying and dividing two float variables
float_one = 15
float_two = 4
print(float_one * float_two)
60
print(float_one / float_two)
3.75

# example 3: multiplying and dividing floats and integers
flt = 18.5
num = 2
print(flt * num)
37.0
print(flt / num)
9.25

bill = 56.25
tip = 5
bill_total = bill + tip
print(bill_total)

bill_split = bill_total/4
print(bill_split)

print(15 / 7)
print(15 // 7)
print(15 / -7)
print(15 // -7)
print(22 % 2)
print(56 % 2)

# odd numbers
print(21 % 2)
print(57 % 2 )

seconds = 15000
hours = seconds // 3600
seconds_remaining = seconds % 3600
minutes = seconds_remaining // 60
print(f"It will take {hours} hours and {minutes} minutes.")
 
savings = 450
deposit = 100
withdrawal = 80


# Write your code below this comment to add a deposit to savings
savings += deposit
print(f"Savings after deposit: {savings}")


# Write your code below this comment to subtract a withdrawal from savings
savings -= withdrawal
print(f"Savings after withdrawal: {savings}")

base_a = 10 
base_b = 14 
height = 5 

area = ((base_a + base_b) * height) / 2 
print(f"The area of the trapezoid is {area} inches") 

print(5 > 4 and 3 == 2 + 1)
print(5 > 4 and 3 != 2 + 1)

x = 5
print(type(x) is int)
print(type(x) is str)
print(type(x) is not str)

print("Hello" in "Hello World")
print("hello" in "Hello World")
print("Goodbye" not in "Hello World")
x = "Hello World"
print("h" not in x)
x = 123
print(type(x) is int)
x = "123"
print(type(x) is int)