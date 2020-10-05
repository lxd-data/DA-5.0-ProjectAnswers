import pandas as pd
import numpy as np

data = ["Amy", "Angie", " Calder", "Dan", "Lauren", "Leif"]
pd.Series(data)

["3D", 2.50, "hello", "$$", 37] 
[3, 565, 92, 34, 56]
[3.21, 4.89, 3.1, 4.0, 6.111]
[True, False, False]
[1, 0, 1, 1, 1, 0]
["2005-05-11", "2006-05-11", "2007-05-11"]

data = np.array([[1, "a"], [2, "b"], [3, "c"], [4, "d"]])
pd.DataFrame(data, columns = ["123", "abc"])

schedule_df = pd.DataFrame([["Gym", "7AM"]], columns=["Activity", "Time"], dtype=str, index=[1])
schedule_df

pd.read_csv('my_file.csv', sep="\t", header=None, names=["Name", "Age", "Height"])

pollution_df = pd.read_csv("my_file.csv")

pollution_df.head()

titanic_df = pd.read_csv("my_file.csv")
titanic_df.head(2)

titanic_df = pd.read_csv("my_file.csv")
titanic_df.tail(3)

titanic_df = pd.read_csv("my_file.csv")
titanic_df.shape

titanic_df = pd.read_csv("my_file.csv")
