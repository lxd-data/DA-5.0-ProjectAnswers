residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]
# A list of lists representing the ages of individuals in a household
residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]

# Example 1: Will return an entire sublist
print(residents_ages[0])

# Example 2: Will return the first age in the second sublist
print(residents_ages[1][0])
# Example 1 Output
[14,15,18,50,54]

# A list of lists representing the ages of individuals in a household
residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]

for household in residents_ages:
    print(household)

# A list of lists representing the ages of individuals in a household
residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]

for household in residents_ages:
    for age in household: # iterates over the ages in each sublist
        print(age)
for household in residents_ages:
    for household in residents_ages:
        for age in household:
            print(age)

num_list = [1, 2, 3, 4, 5]
alpha_list = ['a', 'b', 'c']

# A list of quiz grades grouped by student
quiz_grades = [[56, 74, 82], [97, 65, 87], [88, 92, 93], [82, 74, 79]]


for student in quiz_grades:
    for grade in student:
        print(grade)

quiz_grades = [[56, 74, 82], [97, 65, 87], [88, 92, 93], [82, 74, 79]]

# Empty list to hold letter grades for all students
letter_grades = []

for student in quiz_grades:
    # An empty list to translate the grades for each student
    student_grade = []
    for grade in student:
        if grade >= 90:
            student_grade.append("A")
        elif grade >= 80:
            student_grade.append("B")
        else:
            student_grade.append("<80")
    letter_grades.append(student_grade)

residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]


residents_ages = [[14,15,18,50,54], [9,9,39,42], [25,22,55,54], [25,28], [2,1,28,30]]

# Calculates the number of eligible voters per household
def number_of_voters(neighborhood):
    # A list to hold the number of eligible voters for each household.
    eligible_voters = []
    
    for house in neighborhood: 
        can_vote = 0
        for age in house:  
           if age >= 18:
               can_vote +=1
        eligible_voters.append(can_vote)
    
    return eligible_voters

print(number_of_voters(residents_ages))

patients = [[60, 72, 65, 78], [75, 80, 90, 87], [60, 62, 60, 65], [70, 75, 72, 68]]
for record in patients:
    sum_hr = 0
    for heart_rate in record:            
        sum_hr += heart_rate 
    average_hr = sum_hr/len(record)
    print(average_hr)

for record in patients: # outer loop to iterate over each patient
  sum_hr = 0 # counter to add each hr to
  for heart_rate in record: # inner loop to iterate over each heart rate
    sum_hr += heart_rate 
  average_hr = sum_hr/len(record) # calculate average when inner loop completes
  print(average_hr)

numbers = [3, 6, 9, 12, 15]
over_ten = []

for num in numbers:
    if num > 10:
       over_ten.append(num)

print(over_ten)

numbers = [3, 6, 9, 12, 15]

over_ten = list(filter(lambda x: x>10, numbers))
print(over_ten)

numbers = [3, 6, 9, 12, 15]

over_ten = [num for num in numbers if num > 10]
print(over_ten)

# List comprehension with a string
my_string = "Python"
string_chars = [char for char in my_string]

# Output
['P', 'y','t', 'h', 'o', 'n']


# List comprehension with range()
triple_range = [num * 3 for num in range(0,10)]

# Output 
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

numbers = [2,4,6,8,10]

m = list(map(lambda num: num ** 2, numbers))

numbers = [2,4,6,8,10]

m = [num ** 2 for num in numbers]

numbers = list(range(0,30))
plus_one = [num + 1 for num in numbers]

string_numbers = [str(num) for num in numbers]
print(string_numbers)

customer_id = [1023.0, 1024.0, 1025.0, 1026.0, 1027.0, 1028.0, 1029.0, 1030.0, 1031.0, 1032.0, 1033.0, 1034.0, 1035.0, 1036.0, 1037.0, 1038.0, 1039.0, 1040.0, 1041.0, 1042.0, 1043.0, 1044.0, 1045.0, 1046.0, 1047.0, 1048.0, 1049.0, 1050.0, 1051.0, 1052.0, 1053.0, 1054.0, 1055.0]

def clean_ids(id_list):
    return [int(cust_id) for cust_id in id_list]

print(clean_ids(customer_id))
print([(num-5)**2 for num in numbers])

temp_celsius = [23, 27, 32, 36, 41]
temperature_fahr = []

for temperature in temp_celsius:
    fahr = (temperature * 9/5) + 32
    temperature_fahr.append(fahr)

[(c*9/5) + 32 for c in temp_celsius]
pathstream = [num for num in range(100) if num % 5 == 0 if num % 3 == 0]

path = [num for num in range(100) if num % 5 == 0]
pathstream = ["pathstream" if num % 15 == 0 else num for num in range(100)]

pathstream = ["pathstream" if num % 15 == 0 else "path" if num % 3 == 0 else "stream" if num % 5 == 0 else num for num in range(100)]

def pathstream(num):
    if num % 15 == 0:
        return "pathstream"
    elif num % 3 == 0:
        return "path"
    elif num % 5 == 0:
        return "stream"
    else:
        return num

pathstream_list = [pathstream(num) for num in range(100)]
def negatives_only(prices):
    return [p for p in prices if p < 0]

def increase_price(prices):
    return [round(p*1.10,2) for p in prices if p > 0]

def clean_pricelist(prices):
    return [0 if p < 0 else p for p in prices]
nested_list = [[0,1,2,3],[4,5,6,7], [8,9,10,11]]
flat_list = []

for sublist in nested_list: # Iterate over the sublists
    for item in sublist:  # Iterate over the items in each sublist
        flat_list.append(item) 

print(flat_list)
nested_list = [[0,1,2,3],[4,5,6,7], [8,9,10,11]]

flat_list = [item for sublist in nested_list for item in sublist]

nested_list = [["a","b"], ["c","d"]]

new_list = [item*2 for sublist in nested_list for item in sublist]

matrix = [[0, 1, 2, 3, 4], 
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]

matrix = []

for row in range(5): 
    new_row = [] # creating the sublist 
    for num in range(5): 
        new_row.append(num) # adding numbers to sublist
    matrix.append(new_row) # add sublist to matrix       
print(matrix)

matrix = [[col for col in range(5)] for row in range(5)]

box_measurements_in = [[18, 18, 16],
                       [18, 18, 24],
                       [16, 12, 12],
                       [24, 20, 46]]

box_measurements_cm = [[item * 2.54 for item in sublist] for sublist in box_measurements_in]
print(box_measurements_cm)

matrix = [[0,1], [2,3], [4,5]] 
transposed_matrix = []

for i in range(len(matrix)-1):
  transposed_row = []
  for row in matrix:
    transposed_row.append(row[i])
  transposed_matrix.append(transposed_row)

# Output 
[[0, 2, 4], [1, 3, 5]]


matrix = [[0,1],[2,3],[4,5]]

transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix)-1)]

# Output
[[0, 2, 4], [1, 3, 5]]

population_by_country = [
    ["Year", 2017, 2018, 2019],
    ["Canada", 36.54, 37.06, 37.59],
    ["US", 325.1, 327.2, 328.2],
    ["UK", 65.82, 66.27, 66.65]
]

transposed_population = [['Year', 'Canada', 'US', 'UK'], 
                         [2017, 36.54, 325.1, 65.82], 
                         [2018, 37.06, 327.2, 66.27], 
                         [2019, 37.59, 328.2, 66.65]]
new_list = [[col for col in range(3)] for row in range(3)]
print(new_list)
new_list = [[row[i] for row in nested_list] for i in range(len(nested_list))]

nested_list = [[0,1,2,3],[4,5,6,7], [8,9,10,11]]
flat_list = []

for sublist in nested_list: # Iterate over the sublists
    for item in sublist:  # Iterate over the items in each sublist
        flat_list.append(item) 

print(flat_list)

# Output
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

planets = [["Mercury", 57.91], ["Venus", 108.2], ["Earth", 149.6],["Mars", 227.9],["Jupiter", 778.5]]

distant_planets = [planet for sublist in planets for planet in sublist if sublist[1] > 149.6]

distant_planets = []
for sublist in planets:
    distance = sublist[1]
    if distance > 149.6:
        for details in sublist:
            distant_planets.append(details)