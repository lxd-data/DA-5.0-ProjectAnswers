import numpy as np
np.array([2, 3, 5, 8, 13], dtype = float)

my_first_array = np.array([9,7,6,7,8,3,5])
print(my_first_array)

my_second_array = np.array([0.4, 18.7, 3.3335, 7])

np.array([2, 3, 5, 8, 13], dtype = float)

my_third_array = np.array([1, 2, "dog", 7, 9.3])
np.array([3, 4, 5.5, 6])
my_array = np.array([44.4, 98.3, 17.9], dtype=str)
my_array[2]
my_array[0].dtype

a_two_d_array = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])

np.array([[1.1, 2.1], [3.1, 4.1], [5.1, 6.1], [7.1, 8.1], [9.1, 10.1]])
my_array2 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
my_array3 = np.array([[1], [2], [3], [4]])

np.arange(5) 

to_nine = np.arange(10)

from_five_to_thirteen = np.arange(5, 14) # using start and stop

count_by_fives = np.arange(0, 100, 5) # using start, stop and step

count_by_fives_alt = np.arange(100, step=5)

np.zeros((2, 3))

four_zeros = np.zeros(4)

two_by_three_zeros = np.zeros((2,3))

np.arange(10, 21)
np.arange(500, 1000, 20)
np.zeros(16)
np.zeros((2, 6))

my_first_array = np.array([1, 2, 3, 4, 5, 6, 7])

new_two_d = np.array([[4,1,2,8], [9,1,3,6]])
np.array([[1,2], [3,4], [5,6]]).shape
new_two_d = np.array([[4,1,2,8], [9,1,3,6]])
my_first_array = np.array([1, 2, 3, 4, 5, 6, 7])

x = np.array([[1, 5],
                  [3, 9],
                  [9, 7],
                  [2, 5]])
x = np.array([[1, 5],
                  [3, 9],
                  [9, 7],
                  [2, 5]])

x = np.array([[1, 5],
                  [3, 9],
                  [9, 7],
                  [2, 5]])

np.sort(np.array([4,2,3,6,1]))

my_second_array = np.array([6, 3, 6, 2, 2, 9, 1])

array_1 = np.array([3, 1, 2])
np.sort(array_1)

array_2 = np.array([3, 1, 2])  

arr_1 = np.array([44, 32, 90, 15, 70])
arr_1 = np.array([44, 32, 90, 15, 70])

another_2d_array = np.array([[3, 6.1, 2.11],[4, 7.1, 9.11], [9, 4.1, 2.11]])

np.sort(another_2d_array)

np.sort(another_2d_array, axis = 0)
np.sort(another_2d_array, axis = 1)

np.sort(another_2d_array, axis = None)


arr_1 = np.array([0.0,0.1,0.2,0.3,0.4])
arr_1 = np.array([0.0,0.1,0.2,0.3,0.4])
arr_1 = np.array([0.0,0.1,0.2,0.3,0.4])
arr_1 = np.array([0.0,0.1,0.2,0.3,0.4])
arr_1 = np.array([0.0,0.1,0.2,0.3,0.4])    

arr_1[4]
arr_1[2:10]
arr_1[::5]
arr_1[1:7:4]
two_d_arr = np.array([[0.0,0.1], [0.2,0.3], [0.4,0.5]])
x = np.array([[ 50,  51,  52,  53,  54,  55,  56,  57,  58,  59],
       [ 60,  61,  62,  63,  64,  65,  66,  67,  68,  69],
       [ 70,  71,  72,  73,  74,  75,  76,  77,  78,  79],
       [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89],
       [ 90,  91,  92,  93,  94,  95,  96,  97,  98,  99],
       [100, 101, 102, 103, 104, 105, 106, 107, 108, 109],
       [110, 111, 112, 113, 114, 115, 116, 117, 118, 119],
       [120, 121, 122, 123, 124, 125, 126, 127, 128, 129],
       [130, 131, 132, 133, 134, 135, 136, 137, 138, 139],
       [140, 141, 142, 143, 144, 145, 146, 147, 148, 149]])

my_first_list = [9,7,6,7,8,3,5]

# for loop 
for i, num in enumerate(my_first_list):
    my_first_list[i] = num * 2

# map()
def times_two(num):
    return num * 2

doubles = list(map(times_two, my_first_list))

# list comprehension 
doubles = [num * 2 for num in my_first_list]

a = np.array([1,2,3])
b = 5
c = a * b
