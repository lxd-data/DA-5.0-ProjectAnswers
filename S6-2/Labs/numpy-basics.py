import numpy as np

# TASK 1
array_1 = np.array([2, 3, 4, 5], dtype=float)
array_2 = np.array([[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]])
array_3 = np.array(np.arange(0, 16))
array_4 = np.array(np.arange(0, 100, 7))

# TASK 2
access_1 = array_1[2]
access_2 = array_3[-2]
access_3 = array_4[5:9]
access_4 = array_4[2::3]
access_5 = array_2[2:][0]
access_6 = array_2[:, 1]
access_7 = array_2[:, 1:4] # won't pass

# TASK 3
mask_1 = array_4 % 2 == 0
mask_2 = array_4[array_4 > 50]
mask_3 = array_2[array_2 % 2 == 0]

# TASK 4
names = np.array(["Susie", "Mikayla", "Carlos", "Thao", "Ahmed"])

wages = np.array([15.50, 35.00, 23.40, 18.75, 54.00])
over_20 = names[wages > 20.00]
