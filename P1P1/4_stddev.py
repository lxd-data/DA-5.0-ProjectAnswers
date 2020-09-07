import data_generator as dg # Creates a random list of int between -5 and 10. 
data = dg.data_set # Assigns the list of random int to a variable data

# from earlier
data_sum = 0
for num in data:
    # could also yuse `data_sum = data_sum + num`
    data_sum += num
# this is the mean
average = data_sum/len(data)


sum_squared_diff = 0
for num in data:
    # now calc the sum of (each number minus the mean)^2
    squared_diff = (num - average)**2
    sum_squared_diff += squared_diff
# then, divide by len() to get the sum of mean squared    
mean_squared_diff = sum_squared_diff/len(data)
sd = mean_squared_diff**.5

print(f'The standard deviation of your data is {sd}')
