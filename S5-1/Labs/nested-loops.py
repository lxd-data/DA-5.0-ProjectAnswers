census_data = {
    'household_id': [1,2,3,4], 
    'household_address': ["4824 Poplar Street, Neoga, Illinois","4829 Poplar Street, Neoga, Illinois‌","4832 Poplar Street, Neoga, Illinois", "4837 Poplar Street, Neoga, Illinois"],
    'number_of_residents': [5,4,4,6], 
    'residents_ages':[[14,15,18,50,54],[9,9,39,42],[2,4,38,39],[9,12,17,54,58,81]]
}

#Task 1: Write your code to complete Task 1 below this comment.
def get_house_numbers(data):
    '''Searches the addresses of households and extracts their house number, returning them as list of integer values'''
    addresses = data['household_address']
    all_house_numbers= []
    for address in addresses:
        house_numbers = ""
        for character in address:
            if character.isdigit():
                house_numbers += character
        final_number = int(house_numbers)
        all_house_numbers.append(final_number)
    return all_house_numbers

#---1

# Task 2: Write your code to complete Task 2 below this comment.
def count_children(data):
    '''count the number of children and adults in each household and return it as a dictionary.'''
    all_ages = {
        'children': [],
        'adults': []
    }
    house_ages = data['residents_ages']
    for ages in house_ages:
        child_count = 0
        adult_count = 0
        for age in ages:
            if age >= 18:
                adult_count += 1
            else:
                child_count += 1
        all_ages['adults'].append(adult_count)
        all_ages['children'].append(child_count)
    return all_ages