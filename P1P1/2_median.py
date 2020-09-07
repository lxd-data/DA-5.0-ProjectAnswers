import data_generator as dg # Creates a random list of int between -5 and 10. 
data = dg.data_set # Assigns the list of random int to a variable data

"""1. One way:"""
sorted_data = sorted(data)
length = len(sorted_data)

if length % 2 == 0:
    # if length is even
    mid_val_one = sorted_data[length//2]
    mid_val_two = sorted_data[length//2-1]
    median = (mid_val_one + mid_val_two)/2
    print(f"The median of your data is {median}")
else:
    # if length is odd
    median = sorted_data[len(sorted_data)//2]
    print(f"The median of your data is {median}")

"""2. They could also do this:"""
sorted_data = sorted(data)

if len(sorted_data) % 2 == 0:
    # if length is even
    mid_val_one = sorted_data[len(sorted_data)//2]
    mid_val_two = sorted_data[len(sorted_data)//2-1]
    median = (mid_val_one + mid_val_two)/2
    print(f"The median of the dataset is {median}")
else:
    # if length is odd
    median = sorted_data[len(sorted_data)//2]
    print(f"The median of the dataset is {median}")
    
