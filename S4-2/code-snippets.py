min([4,10,8,6,16,2])

min("Apple")


min(10, 5, 15)

min(26, 20, 19)

min([23, 24, 24, 25, 26, 26, 10, 19, 20, 21, 22, 22])

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]
def signup_stats(signups):
    max_signups = max(signups)
    min_signups = min(signups)

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]
def signup_stats(signups):
    max_signups = max(signups)
    min_signups = min(signups)
    signups_range = max_signups - min_signups

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]

def signup_stats(signups):
    max_signups = max(signups)
    min_signups = min(signups)
    signups_range = max_signups - min_signups

    return f"Max: {max_signups}, Min: {min_signups}, Range: {signups_range}"

print(signup_stats(new_monthly_signups))

sorted([23, 24, 24, 25, 26, 26, 10, 19, 20, 21, 22, 22])

sorted([23, 24, 24, 25, 26, 26, 10, 19, 20, 21, 22, 22], reverse=True)

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]

def sort_signups(signups):
    sorted_signups = sorted(signups)
    list_length = len(signups)

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]

def sort_signups(signups):
    sorted_signups = sorted(signups)
    list_length = len(signups)

    median_one = sorted_signups[list_length // 2]
    median_two = sorted_signups[(list_length // 2)-1]

new_monthly_signups = [225, 100, 125, 427, 568, 679, 800, 523, 354, 300, 219, 196]

def sort_signups(signups):
   sorted_signups = sorted(signups)
   list_length = len(signups)

   median_one = sorted_signups[list_length // 2]
   median_two = sorted_signups[(list_length // 2)-1]

   return f"Median: {(median_one + median_two)//2}"

print(sort_signups(new_monthly_signups))

def avg_signups(signups):
    list_length = len(new_monthly_signups)
    list_sum = sum(new_monthly_signups)

def avg_signups(signups):
    list_length = len(signups)
    list_sum = sum(signups)
    
    return f"The average sign ups last year are: {list_sum / list_length}"

print(avg_signups(new_monthly_signups))

max(1,-2,3,4,5,-10)

iterable_one = [1,2,3]
iterable_two = ["Jan", "Feb", "Mar"]

for one,two in zip(iterable_one, iterable_two):
    print(one, two)

z = zip(iterable_one, iterable_two)

sales_east = [550, 287, 510, 891, 341, 663, 812]
sales_west = [651, 254, 901, 796, 205, 522, 966]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


for east, west in zip(sales_east, sales_west):
    print(east - west)
sales_dict = dict(zip(weekdays, sales_east))
print(sales_dict)


list_one = [1,2,3,4]
list_two = ["a", "b", "c", "d"]

zip_dict = dict(zip(list_one, list_two))
print(zip_dict)

def filter_negatives(nums):
    new_list = []
    
    for num in nums:
        if num >= 0:
            new_list.append(num)
    
    return new_list

def above_zero(num):
    return num >= 0
     
positives = list(filter(above_zero, [-1,-3,-5,2,4]))
print(positives)
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

def filter_odd_num(num):
   return (num % 2) == 0

evens_only = filter(filter_odd_num, numbers)

print(f"The even numbers are: {list(evens_only)}")

percentages = ["90.0%", "89.9%", "95%"]

def convert_to_float(num):
    return float(num[:-1])/100

float_list = list(map(convert_to_float, percentages))
print(float_list)

def remove_tax(sale):
    return round(sale/1.10, 2)

before_tax_east = list(map(remove_tax, sales_east))
before_tax_west = list(map(remove_tax, sales_west))

print(f"East: {before_tax_east}")
print(f"West: {before_tax_west}")

my_list = [6,8,10,12,14,16,18,20,22,24,26,28,30]
def divide_in_half(num):
    return  num/2

halved = list(map(divide_in_half, my_list))
print(halved)

# Function to square a given number
def square_num(num):
    return num ** 2

square_num(6)

# The same function written as a lambda
s = lambda x : x ** 2
s(6)

numbers = [1,2,3,4]

def square_num(num):
    return num ** 2

square_numbers = map(square_num, numbers)

numbers = [1,2,3,4]

square_numbers = map(lambda x : x**2, numbers)

product = lambda a,b : a * b
print(product(3, 5))

increase_age = lambda age: age + 1

spell_check = lambda name: name[:-1]

numbers = [-10, 5, 11, -2, -4, 9]

def filter_negatives(num):
    return num >= 0

positive_list = list(filter(filter_negatives, numbers))
print(positive_list)

numbers = [-10, 5, 11, -2, -4, 9]

positive_list = list(filter(lambda x: x>=0, numbers))
print(positive_list)

list(filter(lambda x: x//3, numbers))

list(filter(lambda x: x%3 == 0, numbers))

list(filter(lambda x: x%3, numbers))


numbers = [2,4,6,8,10]

def square_num(num):
    return num**2

m = map(square_num, numbers)
print(list(m))

numbers = [2,4,6,8,10]

m = list(map(lambda x: x**2, numbers))
print(m)

numbers = [36, 12, 18, 24, 30, 42]

x = list(map(lambda n : n//6, numbers))

user_devices = [
  ["Samsung Galaxy", "Android"],
  ["Macbook Air", "Desktop"],
  ["iPhone X", "iOS"],
  ["Macbook Pro", "Desktop"],
  ["Pixel 3S", "Android"],
  ["iPhone 8", "iOS"],
  ["Surfrace Pro", "Desktop"],
  ["ASUS Laptop", "Desktop"],
  ["iPad Pro", "iOS"],
]

user_devices = [
  ["Samsung Galaxy", "Android"],
  ["Macbook Air", "Desktop"],
  ["iPhone X", "iOS"],
  ["Macbook Pro", "Desktop"],
  ["Pixel 3S", "Android"],
  ["iPhone 8", "iOS"],
  ["Surfrace Pro", "Desktop"],
  ["ASUS Laptop", "Desktop"],
  ["iPad Pro", "iOS"],
]
