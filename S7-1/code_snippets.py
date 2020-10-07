import numpy as np 
import pandas as pd

example_array = np.array([[4, 7, 1], [4, 9, 1], [10, 3, 8], [2, 7, 3]])
example_array[2,1]

df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
df.iloc[1]

df.iloc[:,2]

print("volunteers_df shape: ", df.shape)

# volunteers_df = pd.read_csv("volunteers.csv")
# volunteers_df
# volunteers_df.iat[5,2]
# volunteers_df.loc[4:5, "name":"occupation"]
# volunteers_df.iloc[1:3, 1:3]
# volunteers_df.loc[:6, "occupation":"hours"]

arr = np.array([60, 45, 54, 19, 90, 77, 42])
mask = arr%15 == 0
print(
    arr[mask]
)

print(
    arr[arr%15 == 0]
)

# pollution_df = pd.read_csv("pollution_ca_2012_2016.csv")
# pollution_df.head(3)

# vville_mask = pollution_df["City"] == "Victorville"

# vville_df = pollution_df.loc[vville_mask]

# low_co_df = pollution_df.loc[pollution_df["CO Mean"] < 0.3]

# pollution_df.loc[pollution_df["Site Num"] == 306]

ages_30s = np.arange(30, 40)
print(
    ages_30s    
)

# # Insert code here
# pollution_df = pd.read_csv("pollution_ca_2012_2016.csv")
# pollution_df.head()

# # Insert code here
# pollution_df["SO2 Mean"] < 0.05

# # Insert code here
# pollution_df["CO Mean"] < 0.01

# # Insert code here
# pollution_df.loc[(pollution_df["SO2 Mean"] < 0.05) & (pollution_df["CO Mean"] < 0.01)]

# # Insert code here
# pollution_df.loc[(pollution_df["City"].isin(["Burbank", "Rubidoux"])) &
#                  (pollution_df["NO2 Mean"] > 50)]

# # Insert code here
# san_bern_df = pollution_df.loc[(pollution_df["County"] == "San Bernardino") & 
#                  ((pollution_df["NO2 Mean"] > 10) | 
#                   (pollution_df["SO2 Mean"] > 2))]

# volunteers_df = pd.read_csv("volunteers.csv")
# volunteers_df

# # Insert code here
# volunteers_df.loc[volunteers_df["occupation"].str.contains("driver")]

# # Insert code here
# volunteers_df.loc[(volunteers_df["occupation"].str.contains("driver")) |
# (volunteers_df["occupation"].str.contains("student"))]                  

# # Insert code here
# volunteers_df.loc[volunteers_df["city"].str.startswith("San")]

