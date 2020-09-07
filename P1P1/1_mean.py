import data_generator as dg
data = dg.data_set

# check still passed if data_sum != 0
data_sum = 0
for num in data:
    # could also yuse `data_sum = data_sum + num`
    data_sum += num
print(f"The mean of the dataset is {data_sum/len(data)}")


