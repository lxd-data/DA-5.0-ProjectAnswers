price_per_night = 149
room_type = "Private room"
neighborhood = "Brooklyn"
message = f"The room price is {price_per_night} USD"

if price_per_night < 150:
    message = f"This accommodation is affordable for {neighborhood}."
    # Remove this comment and write your nested if-statement here
    if price_per_night == "Private Room" or room_type ==  "Entire home/apt":
        message = f"This {room_type} is affordable for {neighborhood}. You should book it."

print(message)

price_per_night = 160
room_type = "Private room"
neighborhood = "Brooklyn"
message = f"The room price is {price_per_night} USD"


if price_per_night < 150:
    message = f'This accomodation is affordable for the {neighborhood}.'
    if room_type == "Private room" or room_type == "Entire house/apt":
        message = f"This {room_type} is affordable for {neighborhood}. You should book it."
    else:
        message = "This accommodation is affordable, but it isn't the right type"

else:
    message = "This accomodation is outside your budget"

print(message)


price_per_night = 160
room_type = "Private room"
neighborhood = "Manhattan"
message = f"The room price is {price_per_night} USD"


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


number_list = [3, 6, 9, 12, 15]
for num in number_list:
    num_squared = num**2
    print(num_squared)

number_list = [3, 6, 9, 12, 15]
squared_num = 0
squared_sum = 0

for num in number_list:
    squared_num = num ** 2
    squared_sum += squared_num

print(squared_sum)

# 1: Print the numbers 0-9 using range(), specifying stop only
for num in range(10):
    print(num)

# 2: Print the numbers 1-10 using range(), specifying start & stop 
for num in range(1,11):
    print(num)

# 3: Print only the even numbers from 1-10 using range(), specifying start, stop & step
for num in range(2,11,2):
    print(num)

customers = ["Lillia Fludd","Kathryn Barahona","Shelly Vartanian","Deanna Acheson","Meggan Fraga","Emerald Kroeger","Clotilde Story","Sachiko Drakeford","Scottie Hines","Letha Law"] 

customers_length = len(customers)
index_list = range(customers_length)

for i in index_list:
    print(i, customers[i])

for i in range(len(customers)):
    print(i, customers[i])

number_list = [3, 6, 9, 12, 15]


for i in range(100):
    if i % 5 == 0 and i % 3 == 0:
        print("Pathstream")
    elif i % 3 == 0:
        print("Path")
    elif i % 5 == 0:
        print("Stream")
    else:
        print(i)

name_seniority_list = [("James Smith", "Analyst"), ("Maria Garcia", "Analyst"), ("Hannah Brown", "Director"), ("Mary Hernandez", "Analyst"), ("Drew Johnson", "Director"), ("Sam Taylor", "Executive"), ("Catherine Jones", "Director"), ("Will Miller", "Executive"), ("Alexis Reilly", "Human Resources"), ("James Ross", "Sales"),("Dillon Davis", "Analyst"), ("Owen Jackson", "Analyst"), ("Margaret Clark", "Analyst"), ("Maria Davis", "Director"), ("Louis Roberts", "Director"), ("Jack Evans", "Sales"), ("Daniel Walker", "Analyst"), ("David Thompson", "Human Resources"), ("Riley Edwards", "Analyst"), ("Zach Martin", "Analyst")]

analysts = []
directors = []
executives = []

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
