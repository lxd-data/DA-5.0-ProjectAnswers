# Import libraries and set style to seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Create DataFrame
avo_df = pd.read_csv("avocado.csv")
avo_df.info()

# Convert Data column and sort DataFrame by Date
avo_df["Date"] = pd.to_datetime(avo_df["Date"])
avo_df.sort_values("Date")


midwest_df = avo_df[(avo_df["region"].isin(
    ["Chicago", "Detroit", "Indianapolis", "Nashville"])) & (avo_df["type"] == "conventional")]
midwest_df

sns.violinplot(x="region", y="4046", data=midwest_df)

avo_stacked_df = pd.read_csv("avocado_stacked.csv")

avo_stacked_df.info()

plt.figure()
plt.title("Midwest City 4046 & 4225 Sales Distribution")
sns.violinplot(x="region", y="units", hue="PLU",
               split=True, data=avo_stacked_df)

fig = plt.figure()
sns.swarmplot(y="4046", x="region", data=midwest_df)

sns.swarmplot(x="region", y="units", hue="PLU", data=avo_stacked_df)

midwest_avo_df = midwest_df[["region", "4046", "4225", "4770"]]

sns.pairplot(midwest_avo_df)

sns.pairplot(midwest_avo_df, hue="region")
