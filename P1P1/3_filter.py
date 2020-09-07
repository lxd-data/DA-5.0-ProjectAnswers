import data_generator as dg # Creates a random list of int between -5 and 10. 
data = dg.data_set # Assigns the list of random int to a variable data

positives = []
for num in data:
    if num >= 0:
        positives.append(num)
    else:
        pass
print(positives)

"""You could also do this"""
positives = []
for num in data:
    if num >= 0:
        positives.append(num)
print(positives)

"""Or this"""
positives = []
for num in data:
    if num >= 0:
        positives.append(num)
    pass
print(positives)

"""Or this"""
positives = []
for num in data:
    if num >= 0:
        positives.append(num)
    else: pass
print(positives)

"""Or this"""
positives = []
for num in data:
    if num >= 0: positives.append(num)
    else: pass
print(positives)