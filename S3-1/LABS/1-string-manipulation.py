col_one = 'ITEM_NUMBER' # Output: 'item_number'
col_two = '  Item_Description ' # Output: 'item_description'
col_three = 'item cost $' # Output: 'item_cost_dollars'

#TASK 1: Press the checkbox to test if the code below is present
new_col_one = col_one.lower()

#TASK 2: Write your code for Task 2 below here.
print(new_col_one)

#TASK 3, 4: Write your code for Tasks 3 and 4 below here.
# either order passes the test
new_col_two = col_two.strip().lower() 
new_col_two = col_two.lower().strip()

# as long as .replace is used, this check will pass. Too lenient?
# the test case checking for the correct output is not working
new_col_three = col_three.replace("$", "dollars").replace(" ", "_")
print(new_col_three)