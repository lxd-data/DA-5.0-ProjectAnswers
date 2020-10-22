import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Import libraries and set style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

avo_df = pd.read_csv("avocado.csv")
print(avo_df.head(10))
print(avo_df.tail(10))
avo_df.info()

# Convert Date and sort DataFrame
avo_df['Date'] = pd.to_datetime(avo_df['Date'])
plt.style.use('bmh')

avo_df = avo_df.sort_values("Date")

tampa_2016_conv = avo_df[(avo_df["region"] == "Tampa") & (
    avo_df["type"] == "conventional") & (avo_df["Date"].dt.year == 2016)]

plt.hist(tampa_2016_conv["Total Volume"], edgecolor="black")
plt.title("Distribution of Avocados Sold in Tampa in 2016")
plt.xlabel("Total Volume")
plt.ylabel("Count")
plt.axvline(np.mean(tampa_2016_conv["Total Volume"]))
plt.annotate(f"Mean: {round(np.mean(tampa_2016_conv['Total Volume']), 2)}", xy=(
    np.mean(tampa_2016_conv["Total Volume"]) + 10000, 10.0))

# Histogram and Boxplot of Tampa Sales
fig, axs = plt.subplots(2, 1)

# Histogram of Total Volume Sold in Tampa in 2016
axs[0].hist(tampa_2016_conv["Total Volume"], edgecolor="black")
axs[0].set_title("Distribution of Avocados Sold in Tampa in 2016")
axs[0].set_ylabel("Count")
axs[0].axvline(np.mean(tampa_2016_conv["Total Volume"]))
axs[0].annotate(f"Mean: {round(np.mean(tampa_2016_conv['Total Volume']), 2)}", xy=(
    np.mean(tampa_2016_conv["Total Volume"]) + 10000, 10.0))

axs[1].boxplot(x=tampa_2016_conv["Total Volume"], vert=False)
axs[1].set_xlabel("Total Volume")

# Histogram and Boxplot of Tampa Sales
fig, axs = plt.subplots(2, 1)

# Histogram of Total Volume Sold in Tampa in 2016
axs[0].hist(tampa_2016_conv["Total Volume"], edgecolor="black")
axs[0].set_title("Distribution of Avocados Sold in Tampa in 2016")
axs[0].set_ylabel("Count")
axs[0].axvline(np.mean(tampa_2016_conv["Total Volume"]))
axs[0].annotate(f"Mean: {round(np.mean(tampa_2016_conv['Total Volume']), 2)}", xy=(
    np.mean(tampa_2016_conv["Total Volume"]) + 10000, 10.0))

axs[1].boxplot(x=tampa_2016_conv["Total Volume"], vert=False)
axs[1].set_xlabel("Total Volume")


# Filter DataFrames
tampa_df = avo_df[(avo_df["type"] == "conventional")
                  & (avo_df["region"] == "Tampa")]
total_us_df = avo_df[(avo_df["type"] == "conventional")
                     & (avo_df['region'] == "TotalUS")]


# Create two lineplots
fig, axs = plt.subplots(2, 1, constrained_layout=True)

axs[0].plot(tampa_df["Date"], tampa_df["Total Volume"])
axs[0].set_title("Tampa Avocado Sales Over Time")
axs[0].axhline(np.mean(tampa_df["Total Volume"]))
axs[1].plot(total_us_df["Date"], total_us_df["Total Volume"])
axs[1].set_title("Total US Avocado Sales Over Time")
axs[1].axhline(np.mean(total_us_df["Total Volume"]))
