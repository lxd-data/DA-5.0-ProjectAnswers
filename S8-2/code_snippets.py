import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

fig, ax = plt.subplots()
fig, axs = plt.subplots()

x = np.linspace(0, 100, 50, dtype=int)
y = np.random.randint(max(x), size=50)

fig, axs = plt.subplots(nrows=3, ncols=1, constrained_layout=True)
axs[0].scatter(x, y)
axs[1].plot(x)
axs[2].plot(y)

fig, axs = plt.subplots(nrows=2)
fig, axs = plt.subplots(2)
fig, axs = plt.subplots(2, 3)
fig, axs = plt.subplots(2, 3, constrained_layout=True)


x = np.linspace(0, 100, 100, dtype=int)
y = np.random.randint(0, 10, size=100)

# subplot creation
fig, axs = plt.subplots(2, 3, constrained_layout=True)
axs[0, 0].scatter(x, y)

fig, axs = plt.subplots(2, 3, constrained_layout=True, figsize=(15, 10))
axs[0, 0].scatter(x, y)
fig, axs = plt.subplots(4, 5, constrained_layout=True)


retail_sales_df = pd.read_csv(
    "https://raw.githubusercontent.com/pathstream-curriculum/Python/master/retail-sales.csv")


def get_dept(dept):
    filtered_df = retail_sales_df.loc[(retail_sales_df["Store"] == "Buffalo") &
                                      (retail_sales_df["Dept"] == dept)]
    return filtered_df


electronics_df = get_dept("Electronics")
housewares_df = get_dept("Housewares")
electronics_df = get_dept("Electronics")
housewares_df = get_dept("Housewares")

fig, axs = plt.subplots(2)
electronics_df = get_dept("Electronics")
housewares_df = get_dept("Housewares")

fig, axs = plt.subplots(2, constrained_layout=True)

electronics_df = get_dept("Electronics")
housewares_df = get_dept("Housewares")

fig, axs = plt.subplots(2, constrained_layout=True)

axs[0].plot(electronics_df["Date"], electronics_df["Weekly_Sales"])
axs[1].plot(housewares_df["Date"], housewares_df["Weekly_Sales"])

electronics_df = get_dept("Electronics")
housewares_df = get_dept("Housewares")

fig, axs = plt.subplots(2, constrained_layout=True, figsize=(8, 8))

axs[0].plot(electronics_df["Date"], electronics_df["Weekly_Sales"])
axs[1].plot(housewares_df["Date"], housewares_df["Weekly_Sales"])

fig, axs = plt.subplots(2, constrained_layout=True, figsize=(8, 8))

axs[0].plot(electronics_df["Date"], electronics_df["Weekly_Sales"], c="b")
axs[1].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], c="r")

fig, axs = plt.subplots(2, constrained_layout=True, figsize=(8, 8))

axs[0].plot(electronics_df["Date"], electronics_df["Weekly_Sales"], c="b")
axs[0].set_title("Electronics Weekly Sales")
axs[0].set_xlabel("Week")
axs[0].set_ylabel("Weekly Sales")

axs[1].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], c="r")
axs[1].set_title("Housewares Weekly Sales")
axs[1].set_xlabel("Week")
axs[1].set_ylabel("Weekly Sales")

fig, axs = plt.subplots(1, 2, sharex=True, sharey=True, figsize=(16, 7))

axs[0].plot(electronics_df["Date"], electronics_df["Weekly_Sales"], c="b")
axs[0].set_title("Electronics Weekly Sales")
axs[0].set_ylabel("Weekly Sales")

axs[1].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], c="r")
axs[1].set_title("Housewares Weekly Sales")

fig, axs = plt.subplots(2, 2, constrained_layout=True)
axs[0, 0].set_ylim(0, 100)
axs[0, 1].set_ylim(100, 200)
axs[1, 0].set_ylim(200, 300)
axs[1, 1].set_ylim(300, 400)

fig, axs = plt.subplots(1, 2, sharex=True, sharey=True,
                        constrained_layout=True, figsize=(16, 8))

axs[0].plot(electronics_df["Date"], electronics_df["Weekly_Sales"], c="b")
axs[0].set_title("Electronics Weekly Sales")
axs[0].set_xlabel("Week")
axs[0].set_ylabel("Weekly Sales")
axs[0].set_ylim(0)

axs[1].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], c="r")
axs[1].set_title("Housewares Weekly Sales")
axs[1].set_xlabel("Week")

fig, axs = plt.subplots(2, constrained_layout=True, figsize=(8, 8))

axs[0].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], c="r")

axs[0].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], color="red")

axs[0].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], c="red")

axs[0].plot(housewares_df["Date"], housewares_df["Weekly_Sales"], color="r")

plt.style.available

plt.style.use("classic")
plt.style.use("default")
plt.style.use("seaborn-pastel")


plt.style.use('classic')

fig, ax = plt.subplots(constrained_layout=True)
ax.plot(housewares_buffalo["Date"], housewares_buffalo["Weekly_Sales"])

ax.set_title("Housewares Dept Weekly Sales Over Time in Buffalo")
ax.set_ylabel("Weekly Sales ($)")

plt.xticks(rotation=45)
fig, ax = plt.subplots()
ax.plot(seattle_df["Date"], seattle_df["Weekly_Sales"], label="Seattle")
ax.plot(buffalo_df["Date"], buffalo_df["Weekly_Sales"], label="Buffalo")
ax.plot(las_vegas_df["Date"], las_vegas_df["Weekly_Sales"], label="Las Vegas")
ax.plot(los_angeles_df["Date"],
        los_angeles_df["Weekly_Sales"], label="Los Angeles")
ax.set_ylabel("Weekly Sales ($)")
ax.set_title("Weekly Electronics Sales for each Store Location (2010)")
ax.legend()
# Original xticks were removed and replaced
ticks = ["2010-01", "2010-06", "2010-12"]
labels = ["January", "June", "December"]
plt.xticks(ticks, labels)

plt.xticks(rotation=60)

fig, ax = plt.subplots()
ax.plot(seattle_df["Date"], seattle_df["Weekly_Sales"], label="Seattle")
ax.plot(buffalo_df["Date"], buffalo_df["Weekly_Sales"], label="Buffalo")
ax.plot(las_vegas_df["Date"], las_vegas_df["Weekly_Sales"], label="Las Vegas")
ax.plot(los_angeles_df["Date"],
        los_angeles_df["Weekly_Sales"], label="Los Angeles")

ax.set_ylabel("Weekly Sales ($)")
ax.set_title("Weekly Electronics Sales for each Store Location")
plt.xticks(rotation=60)
ax.legend(loc=2)

fig, ax = plt.subplots()
ax.plot(seattle_df["Date"], seattle_df["Weekly_Sales"], label="Seattle", lw=2)
ax.plot(buffalo_df["Date"], buffalo_df["Weekly_Sales"], label="Buffalo", lw=2)
ax.plot(las_vegas_df["Date"], las_vegas_df["Weekly_Sales"],
        label="Las Vegas", lw=2)
ax.plot(los_angeles_df["Date"],
        los_angeles_df["Weekly_Sales"], label="Los Angeles", lw=2)

ax.set_ylabel("Weekly Sales ($)")
ax.set_title("Weekly Electronics Sales for each Store Location")
plt.xticks(rotation=60)
ax.legend(loc=2)

fig, ax = plt.subplots()
ax.plot(seattle_df["Date"], seattle_df["Weekly_Sales"], label="Seattle")
ax.plot(buffalo_df["Date"], buffalo_df["Weekly_Sales"], label="Buffalo")
ax.plot(las_vegas_df["Date"], las_vegas_df["Weekly_Sales"], label="Las Vegas")
ax.plot(los_angeles_df["Date"],
        los_angeles_df["Weekly_Sales"], label="Los Angeles", lw=3)

ax.set_ylabel("Weekly Sales ($)")
ax.set_title("Weekly Electronics Sales for each Store Location")
plt.xticks(rotation=60)
ax.legend(loc=2)


fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(x, y, alpha=0.1)
ax.set_title("Consumer Price Index (CPI) VS Unemployment Rate", size=20)
ax.set_xlabel("Consumer Price Index (CPI)", size=15)
ax.set_ylabel("Unemployment Rate", size=15)
ax.set_ylim(0, 10)

# Calculate the Medians
x_med = np.median(x.dropna())
y_med = np.median(y.dropna())

# Add Vertical and Horizontal Lines
ax.axvline(x_med, linestyle="--", linewidth=2.0, color="#CA643B")
ax.axhline(y_med, linestyle="--", linewidth=2.0, color="#CA643B")

# Create Strings for Annotations
x_str = "Median CPI:\n" + str(round(x_med, 3))
y_str = "Median \nUnemployment Rate: " + str(y_med)

# Annotate Main Points
ax.annotate(x_str, (x_med + 1, 9), color="#CA643B")
ax.annotate(y_str, (130, y_med + 0.2), color="#CA643B")


# Create Inference for Annotations
inference1 = "The lower the CPI the occurrence of Unemployment Rate values ranging from about 4-9."
inference2 = "\nThe higher the CPI the larger cluster of Unemployment Rate ranging from about 6-9."
inference3 = "\nGiven our sample of data, unemployment rate appears at lower rates when CPI is lower."

# Include an Inferences Box
ax.annotate("Inferences:", (min(x), 2.3), color="black", size=15)
ax.annotate(inference1 + inference2 + inference3, (min(x), 1),
            color="black", size=12, bbox=dict(fc="white"))

# Insert code here

# Set seaborn as style
sns.set()
