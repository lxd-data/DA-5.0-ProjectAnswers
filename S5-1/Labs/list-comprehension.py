census_data = {
    'household_id': [1,2,3,4], 
    'household_address': ["4824 Poplar Street, Neoga, Illinois","4829 Poplar Street, Neoga, Illinois‌","4832 Poplar Street, Neoga, Illinois", "4837 Poplar Street, Neoga, Illinois"],
    'number_of_residents': [5,4,4,6], 
    'residents_ages':[[14,15,18,50,54],[9,9,39,42],[2,4,38,39],[9,12,17,54,58,81]]
}

def get_years_born(house_ages):
    '''Takes a list of a single household's ages as input, and returns a list of the years they were born.'''
    # this only works if there is no(!!) space on either end of the list comprehension. So, this would not pass:
    return [ 2020- age for age in house_ages ]
    # but this would
    return [2020- age for age in house_ages]
    # this wont pass with space around the operator
    return [2020 - age for age in house_ages]
    # the below two will
    return [2020-age for age in house_ages]
    return [2020- age for age in house_ages]


def get_all_years_born():
    '''Returns a list of lists of the years residents were born, based on their ages'''
    # the below won't pass
    return [ get_years_born(house_ages) for house_ages in census_data['residents_ages'] ]
    # but this will
    return [get_years_born(house_ages) for house_ages in census_data['residents_ages']]

#Task 3: Revise the inner for loop of this function to use a list comprehension.
def get_house_numbers():
    '''Searches the addresses of households and extracts their house number, returning them as list of integer values'''
    addresses = census_data['household_address']
    numbers = []
    for address in addresses:
        #Change to list comprehension:
        number = "".join([char for char in address if char.isdigit()])
        numbers.append(int(number)) # number works too
    return numbers


