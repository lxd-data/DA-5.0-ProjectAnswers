import numpy as np
import pandas as pd
import matplotlib.pyplot as ply

df = ''

df.groupby("column_1").agg({"column_2" : "sum"})
df.describe()
np.mean(df["column_2"])
np.median(df["column_2"])


fig, ax = plt.subplots(figsize=(10,10))
ax.hist(titanic_df["Age"])
ax.set_title("Distribution of Age on the Titanic")
ax.set_ylabel("Count")
ax.set_xlabel("Age")

fig, ax = plt.subplots(dpi=200)
ax.hist(titanic_df["Age"], edgecolor="w")
ax.set_title("Distribution of Age on the Titanic")
ax.set_ylabel("Count")
ax.set_xlabel("Age")


avocado_df.to_csv("new_avocado.csv", index=False)
