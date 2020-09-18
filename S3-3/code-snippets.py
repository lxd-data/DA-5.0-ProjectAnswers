customer_id = [1023.0, 1024.0, 1025.0, 1026.0, 1027.0, 1028.0, 1029.0, 1030.0, 1031.0, 1032.0, 1033.0, 1034.0, 1035.0, 1036.0, 1037.0, 1038.0, 1039.0, 1040.0, 1041.0, 1042.0, 1043.0, 1044.0, 1045.0, 1046.0, 1047.0, 1048.0, 1049.0, 1050.0, 1051.0, 1052.0, 1053.0, 1054.0, 1055.0]

i = 0

customer_id[i]= int(customer_id[i])

for i in range(len(customer_id)):
    customer_id[i]= int(customer_id[i])
print(customer_id)

balance = 10
message = f"BALANCE UPDATE: Account balance is ${balance}"

if balance < 0:
    message = "BALANCE ALERT: Account is overdrawn."
print(message)


price_per_night = 160
room_type = "Private room"
neighborhood = "Brooklyn"
message = f"The room price is {price_per_night} USD"
if price_per_night < 150:
    message = f"This accommodation is affordable for {neighborhood}."
print(message)

# EXAMPLE 1
area_code = 805

if area_code == 805:
    counties = ["Kern", "Monterey", "San Luis Obispo", "Santa Barbara", "Ventura"]
    print(f"The {area_code} area code has {len(counties)} counties")

print(f"{area_code} area code is in California.")


area_code = 415

if area_code == 805:
    counties = ["Kern", "Monterey", "San Luis Obispo", "Santa Barbara", "Ventura"]
    print("The {} area code has {} counties".format(area_code, len(counties)))

print("{} area code is in California.".format(area_code))

balance = float(input("Enter balance:"))
message = f"BALANCE UPDATE: Account balance is ${balance}"

if balance < 0:
    message = "BALANCE ALERT: Account is overdrawn."
if balance < 25 and balance >= 0:
    message = "BALANCE ALERT: Balance is low (under $25)."
print(message)

message = "BALANCE UPDATE: Account balance is ${}".format(balance)

if balance < 0: # outer if statement
    message = "BALANCE ALERT: Account is overdrawn."
    if balance <= -50: # nested if statement 
        message = "ACCOUNT ALERT: Overdraft fee for insufficient funds"
print(message)


if price_per_night < 150:
    message = f"This accomodation is affordable for {neighborhood}."
    if room_type == "Private room" or room_type == "Entire home/apt":
        message = f"This {room_type} is affordable for {neighborhood}."
    else:
        message = "This accomodation is affordable, but it isn't the right type."
else:
    message = "This accomodation is not within your budget."
print(message)


if balance < 0:
    print("BALANCE ALERT: Account is overdrawn.")
    if balance <= -50:
        message = "ACCOUNT ALERT: Overdraft fee for insufficient funds"
    else:
        message = "ACCOUNT ALERT: If account balance is greater than or equal to -$50 an overdraft fee will be applied."
elif balance < 25:
    message = "BALANCE ALERT: Balance is low (under $25)."
else:
    message = f"BALANCE UPDATE: Account balance is ${balance}"


if balance < 0:
    print("BALANCE ALERT: Account is overdrawn.")
    if balance <= -50:
        message = "ACCOUNT ALERT: Overdraft fee for insufficient funds"
    else:
        message = "ACCOUNT ALERT: If account balance is greater than or equal to -$50 an overdraft fee will be applied."
elif balance < 25:
    message = "BALANCE ALERT: Balance is low (under $25)."
else:
    message = f"BALANCE UPDATE: Account balance is ${balance}"

print(message)

if price_per_night < 150:
    message = f'This accomodation is affordable for the {neighborhood}.'
    if room_type == "Private room" or room_type == "Entire house/apt":
        message = f"This {room_type} is affordable for {neighborhood}. You should book it." 
    else:
        message = "This accommodation is affordable, but it isn't the right type"
elif neighborhood == "Brooklyn":
        message = "This accommodation is outside of your budget, but it's in your desired neighborhood"
else:
    message = "You should keep looking"
   
print(message)

list = ["Python", "is", "fun"]
string = "Python"


destinations = ["St. Lucia", "Argentine Patagonia", "Banff"]

for destination in destinations:
   print(f"I am currently in {destination}.")

motto = "Python is fun!" # string
numbers = [55, 57, 59, 61] # list
days = ("Monday", "Wednesday", "Friday") # tuple


my_list = ["item one", "item two", "item three"]

# loop through items directly
for item in my_list:
    print(item)


# loop through items by index
for index in range(len(my_list)):
    my_list[index] = index + 1

my_tuple = ("item one", "item two", "item three")

for item in my_tuple:
    print(item)


my_set = {"item one", "item two", "item three"}

for item in my_set:
    print(item)

my_dict = {
    1: "item one",
    2: "item two",
    3: "item three"
}

for item in my_dict:
    print(item)

my_dict = {
    1: "item one",
    2: "item two",
    3: "item three"
}

for item in my_dict:
    print(my_dict[item])

my_string = "item one"

for char in my_string:
    print(char)

number_list = [3, 6, 9, 12, 15]
number_sum = 0

for num in number_list:
    number_sum += num

print(number_sum)

for num in number_list:
    print(num ** 2)

customer_dictionary = {
        "Dan" : 100,
        "Angie" : 85,
        "Amy" : 92
    }

for customer in customer_dictionary:
    print(customer_dictionary)

string = "Programming is fun!"

for char in string:
    print(char)

for i in range(10):
    print(i)

list_of_ten = [0,1,2,3,4,5,6,7,8,9]

for num in range(5): 
    print(num)

for num in range(1,5): 
    print(num)

# specifying start, stop and step
for num in range(1,10, 2): 
    print(num)


# 1: Print the numbers 0-9 using range(), specifying stop only
for num in range(10):
    print(num)

# 2: Print the numbers 1-10 using range(), specifying start & stop 
for num in range(1,11):
    print(num)

# 3: Print only the even numbers from 1-10 using range(), specifying start, stop & step
for num in range(2,11,2):
    print(num)

# a list containing customer ids
customer_id = [1022.0, 1023.0, 1024.0, 1025.0, 1026.0, 1027.0, 1028.0, 1029.0, 1030.0, 1031.0, 1032.0, 1033.0, 1034.0, 1035.0, 1036.0, 1037.0, 1038.0, 1039.0, 1040.0, 1041.0, 1042.0, 1043.0, 1044.0, 1045.0, 1046.0, 1047.0, 1048.0, 1049.0, 1050.0, 1051.0, 1052.0, 1053.0, 1054.0, 1055.0]

# manually updating customer ids using indices
customer_id[0]= int(customer_id[0])
customer_id[1]= int(customer_id[1])
customer_id[2]= int(customer_id[2])
customer_id[3]= int(customer_id[3])
customer_id[4]= int(customer_id[4])
customer_id[5]= int(customer_id[5])
...
...
customer_id[29]= int(customer_id[29])
customer_id[30]= int(customer_id[30])
customer_id[31]= int(customer_id[31])
customer_id[32]= int(customer_id[32])
customer_id[32]= int(customer_id[33])

customers = ["Lillia Fludd","Kathryn Barahona","Shelly Vartanian","Deanna Acheson","Meggan Fraga","Emerald Kroeger","Clotilde Story","Sachiko Drakeford","Scottie Hines","Letha Law"] 

customers_length = len(customers)
index_list = range(customers_length)

for i in index_list:
    print(i, customers[i])

numbers = [3, 6, 9, 12, 15]
over_ten = []

for num in numbers:
    if num > 10:
       over_ten.append(num)

print(over_ten)

numbers = [3, 6, 9, 12, 15]
over_ten = []
under_ten = []

for num in numbers:
    if num > 10:
       over_ten.append(num)
    else:
        under_ten.append(num)

print(over_ten)
print(under_ten)

numbers = [3, 6, 9, 12, 15]
over_ten = []
under_ten = []
under_five = []

for num in numbers:
    if num > 10:
       over_ten.append(num)
    elif num < 5:
       under_five.append(num)
    else:
        under_ten.append(num)

print(over_ten)
print(under_ten)
print(under_five)


grades = [56, 74, 82, 97, 65, 87, 88, 92, 93, 82, 74, 79, 90, 81]
for grade in grades:
    if grade >= 90:
        print(grade)

for grade in grades:
    if grade >= 90:
        print("A") # print A's
    elif (grade >= 80) & (grade < 90):
        print("B") # print B's

for grade in grades:
    if grade >= 90:
        print("A") # print A's
    elif (grade >= 80) & (grade < 90):
        print("B") # print B's
    else:
        print("Scored below an 80.")

for i in range(100):
    if i % 5 == 0 and i % 3 == 0:
        print("Pathstream")
    elif i % 3 == 0:
        print("Path")
    elif i % 5 == 0:
        print("Stream")
    else:
        print(i)
    
customer_birthdays = [("Josh", "11-22-1995"), ("Nate", "10-07-1990"),("Rose", "3-15-1993"),("Ellie", "6-29-1994"), ("Tiffany", "7-04-1998")]
for customer in customer_birthdays:
    print(customer[1])

for name, birthday in customer_birthdays:
    print(birthday)

my_dict = {1: 'item one', 2: 'item two'}

# Unpack keys only
one, two = my_dict  
print(one)
print(two)

one, two = my_dict.values()  

print(one)
print(two)


grocery_list = ["milk", "butter", "ice cream", "chicken", "broccoli"]
for index, item in enumerate(grocery_list, start = 1):
    print(index)

pets = [("Rudy", "Dog"), ("Carmen", "Cat"), ("Jake", "Dog"), ("Frank", "Hamster")]

for name, pet_type in pets:
    print(pet_type)

sales = [("sunglasses", 7.99, 1500), ("socks", 2.99, 500), ("shoes", 25.99, 355)]

for sale in sales:
    print(f"Income for {sale[0]} is: {sale[1] * sale[2]}")

sales = [("sunglasses", 7.99, 1500), ("socks", 2.99, 500), ("shoes", 25.99, 355)]

for product, price, units_sold in sales:
    print(f"Income for {product} is: {price * units_sold}")

customer_id = [1022.0, 1023.0, 1024.0, 1025.0, 1026.0, 1027.0, 1028.0, 1029.0, 1030.0, 1031.0, 1032.0, 1033.0, 1034.0, 1035.0, 1036.0, 1037.0, 1038.0, 1039.0, 1040.0, 1041.0, 1042.0, 1043.0, 1044.0, 1045.0, 1046.0, 1047.0, 1048.0, 1049.0, 1050.0, 1051.0, 1052.0, 1053.0, 1054.0, 1055.0]

for i in range(len(customer_id)):
    customer_id[i]= int(customer_id[i])

for i, customer in enumerate(customer_id):
    print(i)
    print(customer)
    customer_id[i]= int(customer_id[i])


times_of_day = ["morning", "afternoon", "night"]

enumerate(times_of_day)


# In a for loop
for index, time in enumerate(times_of_day):
    print(index, time)

contestants = ["Adriene Baril", "Ismael Stripling", "Freddie Downey", "Rosana Wescott","Avis Boehman", "Everett Poehler", "Marvin Hasson","Brendan Mazer","Evangeline Sinkler","Tana Bocanegra"]

for place, contestant in enumerate(contestants, 1):
    print(f"{place}. {contestant}")

 

analysts = []
directors = []
executives = []

name_seniority_list = [("James Smith", "Analyst"), ("Maria Garcia", "Analyst"), ("Hannah Brown", "Director"), ("Mary Hernandez", "Analyst"), ("Drew Johnson", "Director"), ("Sam Taylor", "Executive"), ("Catherine Jones", "Director"), ("Will Miller", "Executive"), ("Alexis Reilly", "Human Resources"), ("James Ross", "Sales"),("Dillon Davis", "Analyst"), ("Owen Jackson", "Analyst"), ("Margaret Clark", "Analyst"), ("Maria Davis", "Director"), ("Louis Roberts", "Director"), ("Jack Evans", "Sales"), ("Daniel Walker", "Analyst"), ("David Thompson", "Human Resources"), ("Riley Edwards", "Analyst"), ("Zach Martin", "Analyst")]

for name, title in name_seniority_list:
    if title == "Director":
        directors.append(name)
    elif title == "Executive":
        executives.append(name)
    elif title == "Analyst":
        analysts.append(name)

print(analysts)
print(directors)
print(executives)

my_list = ["one", "two", "three"]

for item in my_list:
   print(f"I am number {item}")

number = 10

while number > 0:
    print(number)
    number -= 1

print("Lift off!")

my_list = []
num = 0

while len(my_list) < 4:
   my_list.append(num)
   num += 1
print(my_list)
funds_raised = 0 # amount of funds raised 

goal = 1000 # fundraising goal

days = 0 # tracking number of days to reach goal

# amount of funds raised
funds_raised = 0

# fundraising goal
goal = 1000

# tracking number of days to reach goal
days = 0

while funds_raised < goal:
    donation = int(input("How many funds came in today?: "))
    funds_raised = funds_raised + donation
    days+=1
    print(f"We've raised {funds_raised} to date. {goal-funds_raised} to go")

print(f"Fundraising goal of {goal} met in {days} days!")

number = 10

while number > 0:
  if number == 5:
    print("It's the final countdown")
  else:
    print(number)
  number -= 1
print("Lift off!")

number = 10

while number > 0:
  if number == 5:
    print("It's the final countdown")
  elif number <= 3:
   print(f"{number}...")
  else:
    print(number)
  number -= 1
print("Lift off!")

# amount of funds raised
funds_raised = 0
# fundraising goal
goal = 1000
# tracking number of days to reach goal
days = 0

while funds_raised < goal:
    donation = int(input("How many funds came in today?: "))
    funds_raised = funds_raised + donation
    days+=1
    if donation >= 50:
        print(f"Thanks to a big donor, we've now raised ${funds_raised}! ${goal-funds_raised} to go")
    else:
        print(f"We've raised ${funds_raised} to date. ${goal-funds_raised} to go")

print(f"Fundraising goal of ${goal} met in {days} days!")

number = 10

while number > 0:
  if number == 3:
      break
  print(number)
  number -= 1

print("Lift off!")

number = 10

while number > 0:
  number -= 1
  
  if number % 2 == 0:
      continue
  print(number)


print("Lift off!")