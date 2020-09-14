avocado_prices = [3.00, 2.99, 4.25, 2.00, 2.50, 1.99]
avocado_prices = [3.00, 2.99, 4.25, 2.00, 2.50, 1.99]
type(avocado_prices)

avocado_prices_one = [3.00, 2.99, 4.25, 2.00, 2.50, 1.99]
avocado_prices_two = [1.99, 2.50, 2.00, 4.25, 2.99, 3.00]
avocado_prices_one == avocado_prices_two

int_list = [1, 2, 3, 4] # all the same type 
int_str_list = ["one", True, 3, 4.00, "five"] # mixed types
empty_list = [] # empty
long_int_list = [0, 1, 2, 3, 4, 5, 6, 7,8 ,9 , 10, 11, 12, 13, 14, 15, 16, 17, 18] # long
repeated_str_list = ["one", "two", "one", "two"] # repeated

avocado_prices = [3.00, 2.99, 4.25, 2.00, 2.50, 1.99]
avocado_prices[1]
avocado_prices[2]

avocado_store_prices = [
    ["Joe's Grocery", 1.99], 
    ["Sunkissed Organics", 4.25], 
    ["Bloor Street Market", 3.00]
]

empty_list = []
number_list = [5,10,15,20]
string_list = ["hickory","dickory","dock"]
nested_list = [["breakfast",9],["lunch", 12], ["dinner", 18]]

sf_coordinates = (37.7749, 122.4194)
sf_coordinates
(37.7749, 122.4194)
type(sf_coordinates)

sf_coordinates_1 = (37.7749, 122.4194)
sf_coordinates_2 = (122.4194, 37.7749)
sf_coordinates_1 == sf_coordinates_2

int_tuple = (1,2,3,4,5) # all the same type
str_int_tuple = ("one", True, 3, 4.00, "five") # mixed types
empty_tuple = () # empty
long_int_tuple = (0,2,3,4,5,6,7,8,9,10,11,12,13,14,15) # long
repeated_str_tuple = ("one", "two", "one", "two") # repeated 

avocado_prices = (3.00, 2.99, 4.25, 2.00, 2.50, 1.99)
avocado_prices[1]
avocado_prices[2]

avocado_store_prices = (
    ("Joe's Grocery", 1.99), 
    ("Sunkissed Organics", 4.25), 
    ("Bloor Street Market", 3.00)
)


# With a trailing comma:
my_tuple = ("a", )
type(my_tuple)

# Without the comma:
my_tuple = ("a")
type(my_tuple)

# creating a tuple from a string
t = tuple("San Francisco")

# creating a tuple from a list
t2 = tuple(["Monday", "Wednesday", "Friday"])

empty_tuple = ()
number_tuple = (5,10,15,20)
string_tuple = ("hickory","dickory","dock")
nested_tuple = (("breakfast",9),("lunch", 12), ("dinner", 18))

cali_coordinates = [(37.7749, 122.4194), (32.7157, 117.1611), (34.0522, 118.2437)]
print(cali_coordinates)
cali_coordinates = [[37.7749, 122.4194], [32.7157, 117.1611], [34.0522, 118.2437]]
print(cali_coordinates)

my_dictionary = {
      "key_one": "value",
      "key_two": "value",
      "key_three": "value"
    }
address_book = {
    "Molly": "202-555-0158",
    "Anjit": "202-555-0175",
    "Juan" : "202-555-0138",
    "Cheyenne" : "202-555-0108"
}

address_book = {
    "Molly": "202-555-0158",
    "Anjit": "202-555-0175",
    "Juan" : "202-555-0138",
    "Cheyenne" : "202-555-0108"
}
address_book_2 = {
    "Juan" : "202-555-0138",
    "Anjit": "202-555-0175",
    "Molly": "202-555-0158",
    "Cheyenne" : "202-555-0108"
}

print(address_book == address_book_2)

contact = {
    "Name": "Molly",
    "Phone": "202-555-0175",
    "Age" : 42,
    "Subscriber" : True,
    "Address" : {
        "Street" : "405 Nebraska Ave",
        "City" : "Grand Island",
        "State" : "NE",
        "Zip" : "68801"
    }
}

address_book = {
    "Molly": "202-555-0158",
    "Anjit": "202-555-0175",
    "Juan" : "202-555-0138",
    "Cheyenne" : "202-555-0108"
}

address_book = {
    "Molly": "202-555-0158",
    "Anjit": "202-555-0175",
    "Juan" : "202-555-0138",
    "Cheyenne" : "202-555-0108"
}
address_book_empty = dict()
address_book_empty
{}
address_book = dict([
    ("Molly", "202-555-0158"),
    ("Anjit", "202-555-0175"),
    ("Cheyenne" , "202-555-0108")
])

print(address_book)

empty_dict = dict() 
my_dict = {"name" : "Greg", "age" : 35} 
my_dict_2 = dict([("name", "Greg"), ("age", 25)])
print(my_dict_2)


customer_order = {"jeans", "shirt", "shoes"}
print(type(customer_order))

customer_order_1 = {"jeans", "shirt", "shoes"}
customer_order_2 = {"shirt", "jeans", "shoes"}
print(customer_order_1 == customer_order_2)

customer_order = {"jeans", "shirt", "shoes", "jeans"}
print(customer_order)


# creating an empty set
empty_set = set()
empty_set

# creating a set from a list
customer_order = set(["jeans", "shirt", "shoes"])
customer_order


set("jeans")

empty_set = set() 
customer_order = {"shoes", "shirt"} 
customer_order_2 = set(["shoes", "shirt"])

shirts = set(['John', 'Jane', 'Jack', 'June'])
pants = set(['Jane', 'Jack', 'Susan', 'Zack'])
shirts | pants # using the pipe operator
{'June', 'John', 'Jane', 'Zack', 'Susan', 'Jack'}
shirts.union(pants)# using .union()
{'June', 'John', 'Jane', 'Zack', 'Susan', 'Jack'}

shirts = set(['John', 'Jane', 'Jack', 'June'])
pants = set(['Jane', 'Jack', 'Susan', 'Zack'])
shirts & pants # using the & operator
{'Jack', 'Jane'}
shirts.intersection(pants) # using .intersection()
{'Jack', 'Jane'}

shirts = set(['John', 'Jane', 'Jack', 'June'])
pants = set(['Jane', 'Jack', 'Susan', 'Zack'])
shirts - pants # using the - operator
{'John', 'June'}
shirts.difference(pants) # using .difference()
{'John', 'June'}

a = {1, 2, 3}
b = {3, 4, 5}
c = {5, 6, 7}
d = a & b | c
d
{3, 5, 6, 7}

# Using methods:
a.intersection(b).union(c)
{3, 5, 6, 7}

d = a & (b | c)
d
{3}

b.union(c).intersection(a)
{3}

shirts = set(['John', 'Jane', 'Jack', 'June', 'Zim', 'Jimmy'])
pants = set(['Jane', 'Jack', 'Susan', 'Zack', 'Jonah'])
shoes = set(['Jimmy', 'Jack', 'Jonah', 'Zach', 'Zim'])

shirts = set(['John', 'Jane', 'Jack', 'June', 'Zim', 'Jimmy'])
pants = set(['Jane', 'Jack', 'Susan', 'Zack', 'Jonah'])
shoes = set(['Jimmy', 'Jack', 'Jonah', 'Zach', 'Zim'])

dairy_products = ["milk", "goat cheese", "cream cheese", "whipped cream", "ice cream"]

dairy_products[0] # milk
dairy_products[1] # goat cheese
dairy_products[2] # cream cheese
dairy_products[3] # whipped cream
dairy_products[4] # ice cream

# nested list
dairy_products = [
    ["milk"], 
    ["goat cheese", "cream cheese"],
    ["whipped cream", "ice cream"]
]

dairy_products[0] # ['milk']
dairy_products[1] # ['goat cheese', 'cream cheese']
print(dairy_products[2]) # ['whipped cream', 'ice cream']

# nested list
dairy_products = [
    ["milk"], 
    ["goat cheese", "cream cheese"],
    ["whipped cream", "ice cream"]
]

dairy_products[0][0] # milk
dairy_products[1][0] # goat cheese
dairy_products[1][1] # cream cheese
dairy_products[2][0] # whipped cream 
dairy_products[2][1] # ice cream'

store_items = [
    ["milk", "goat cheese", "ice cream"],
    ["beef", "pork chops", "chicken"],
    ["apple", "orange", "onion"]
]

dairy_products = ["milk", "goat cheese", "cream cheese", "whipped cream", "ice cream"]
dairy_products[0] = "skim milk"


cities = ["Jacksonville", "Phoenix", "San Diego", "Charlotte", "Detroit"]

cities_state = [
    ["Jacksonville", "Florida"],
    ["Phoenix", "Arizona"],
    ["San Diego", "California"],
    ["Charlotte", "North Carolina"],
    ["Detroit", "Michigan"]
]

print(cities[2])
print(cities[-2])
print(cities_state[0][1])
print(cities_state[-1][-2])
cities[2] = "Sacremento"
print(cities)

heights = [["george", 1.75], [ "lisa", 1.62], ["mayouree", 1.55], ["hima", 1.70], ["darius", 1.82]]

dairy_products = ["milk", "goat cheese", "cream cheese", "whipped cream", "ice cream"]
len(dairy_products)
5


len(dairy_products) % 2 == 0 # true if list is even


dairy_products[len(dairy_products)//2] # returns the middle item of odd length list

print(len(cities) % 2 == 0)
print(len(cities) == len(cities_state))
print(cities[len(cities)//2])

dairy_products = ["milk", "goat cheese", "cream cheese", "whipped cream", "ice cream"]
cheese = dairy_products[1:3]
cheese
['goat cheese', 'cream cheese']

dairy_products[:3]
['milk', 'goat cheese', 'cream cheese']
dairy_products[3:]
['whipped cream', 'ice cream']


dairy_products = ["milk", "goat cheese", "cream cheese", "whipped cream", "ice cream"]
dairy_products[1::2]

dairy_products = ["milk", "goat cheese", "cream cheese", "whipped cream", "ice cream"]
dairy_products[1::2]
['goat cheese', 'whipped cream']

daily_sunlight_minutes = [866, 868, 915, 906, 910, 913, 915]
daily_sunlight_minutes.append(917)

daily_sunlight_minutes = [866, 868, 915, 906, 910, 913, 915]
daily_sunlight_minutes.insert(2, 870)


weekly_sunlight_one = [866, 868, 915, 906, 910, 913, 915]
weekly_sunlight_two = [855, 868, 920, 920, 915, 917, 914]
two_weeks_sunlight = weekly_sunlight_one + weekly_sunlight_two
two_weeks_sunlight
[866, 868, 915, 906, 910, 913, 915, 855, 868, 920, 920, 915, 917, 914]

weekly_sunlight_one = [866, 868, 915, 906, 910, 913, 915]
weekly_sunlight_two = [855, 868, 920, 920, 915, 917, 914]
weekly_sunlight_one.extend(weekly_sunlight_two)
weekly_sunlight_one
[866, 868, 915, 906, 910, 913, 915, 855, 868, 920, 920, 915, 917, 914]

daily_sunlight_minutes = [866, 868, 915, 906, 910, 913, 915]
daily_sunlight_minutes.remove(915)
daily_sunlight_minutes
[866, 868, 906, 910, 913, 915]

daily_sunlight_minutes = [866, 868, 915, 906, 910, 913, 915]
del daily_sunlight_minutes[1]
[866, 915, 906, 910, 913, 915] # 868 has been deleted

del daily_sunlight_minutes[2:5]
[866, 868, 913, 915] # 915, 906, and 910 have been deleted

a_list = [5, 3, 8, 1, 6, 8, 9]
a_list.sort()
a_list
[1, 3, 5, 6, 8, 8, 9]

a_list.sort(reverse = True)
a_list
[9, 8, 8, 6, 5, 3, 1]

alphabet_soup = ["a", "a", "b", "c", "d","e","e","f","g","a","b","c"]
alphabet_soup.sort()
alphabet_soup
['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'e', 'e', 'f', 'g']
alphabet_soup.count("c")

a_list = [5, 3, 8, 1, 6, 8, 9]
a_list.sort()
a_list
[1, 3, 5, 6, 8, 8, 9]

a_list.sort(reverse = True)
a_list
[9, 8, 8, 6, 5, 3, 1]


alphabet_soup = ["a", "a", "b", "c", "d","e","e","f","g","a","b","c"]
alphabet_soup.sort()
alphabet_soup
['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'e', 'e', 'f', 'g']
alphabet_soup.count("c")

movie_details = {
    "title": "Back to the Future",
    "director" : "Robert Zemeckis",
    "year_of_release" : 1985,
    "rating" : 8.5,
    "stars" : ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"]
}

movie_details['director']


my_dict = {1:"one", 2: "two"}
my_dict.get(1)
"one"
my_dict.get(3)
# with a default value
my_dict.get(3, "Whoops! Can't find that")
"Whoops! Can't find that!"

movie_details.get('budget') # without default value

movie_details.get('budget', 'whoops, not found!') # with default value
'Whoops, not found!'

cities_population = {
    "Jacksonville": 903889,
    "Phoenix": 1660000,
    "San Diego": 1426000,
    "Charlotte": 872498,
    "Detroit": 672662
}

print(f"The population of Charlotte is {cities_population['Charlotte']}")
print(f"The population of Detroit is {cities_population.get('Detroit')}")
print(cities_population.get('Kentucky', "Sorry I cannot find that city name"))

# BONUS
print(cities_population['Charlotte'] > cities_population['Phoenix'])


movie_details = {
    "title": "Back to the Future",
    "director" : "Robert Zemeckis",
    "year_of_release" : 1985,
    "rating" : 8.5,
    "stars" : ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"]
}

movie_details['rating'] = 8.7 # using the assignment operator
my_dict = {"color_one":"red", "color_two": "blue"}

# using a keyword argument
my_dict.update(color_one = "yellow")
{"color_one":"yellow", "color_two": "blue"}

# using a key-value pair
my_dict.update({"color_one":"yellow"})
{"color_one":"yellow", "color_two": "blue"}

movie_details.update(rating = 8.7) # using the update method

movie_details.update(title = "Back to the Future II", year_of_release = 1989)

movie_details['budget'] = 19000000
movie_details = {
    "title": "Back to the Future",
    "director" : "Robert Zemeckis",
    "year_of_release" : 1985,
    "rating" : 8.5,
    "stars" : ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"],
    "budget" : 19000000
}
del movie_details['rating']
movie_details = {
    "title": "Back to the Future",
    "director" : "Robert Zemeckis",
    "year_of_release" : 1985,
    "stars" : ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"],
    "budget" : 19000000
}

movie_details = {
    "title": "Back to the Future",
    "director" : "Robert Zemeckis",
    "year_of_release" : 1985,
    "stars" : ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"],
    "budget" : 19000000
}

# print(movie_details[1])

movie_details = {
    "title": "Back to the Future",
    "director" : "Robert Zemeckis",
    "year_of_release" : 1985,
    "stars" : ["Michael J. Fox", "Christopher Lloyd", "Lea Thompson"],
    "budget" : 19000000
}

movie_details['year_of_relese'] = 1989

