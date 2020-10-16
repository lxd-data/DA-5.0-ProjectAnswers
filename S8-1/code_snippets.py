import matplotlib as mpl
import numpy as np
import pandas as pd
# # mpl.pyplot.hist(data)
import matplotlib.pyplot as plt
# # plt.hist(data)

# data_x = np.arange(0, 11)
# data_y = np.array([y**2 for y in data_x])
# plt.plot(data_x, data_y)
# # plt.show()

# # plt.scatter(lemonade_df["temp_f"], lemonade_df["sales"])
# fig, ax = plt.subplots()
# fig, ax = plt.subplots()
# # ax.scatter(lemonade_df["temp_f"], lemonade_df["total_sales"])
# plt.scatter(data_x, data_y)
# # fig, ax = plt.scatter()
# # ax(data_x, data_y)

# fig, ax = plt.subplots()
# ax.scatter(data_x, data_y)

# fig, ax = plt.subplots()
# # ax.scatter(lemonade_df["temp_f"], lemonade_df["total_sales"])

# # ax.set_title("Lemonade Sales")

# fig, ax = plt.subplots()
# # ax.scatter(lemonade_df["temp_f"], lemonade_df["total_sales"])

# ax.set_title("Lemonade Sales")
# ax.set_xlabel("Temperature (Fahrenheit)")
# ax.set_ylabel("Sales ($)")
# ax.set_title("Lemonade Sales")
# ax.set_xlabel("Temperature (Fahrenheit)")
# ax.set_ylabel("Sales ($)")

# fig, ax = plt.subplots()
# # ax.scatter(lemonade_df["temp_f"], lemonade_df["total_sales"])

# ax.set_title("Lemonade Sales")
# ax.set_xlabel("Temperature (Fahrenheit)")
# ax.set_ylabel("Sales ($)")
# ax.grid(True) 

# pollution_df = pd.read_csv("https://raw.githubusercontent.com/pathstream-curriculum/Python/master/pollution_ca_2012_2016.csv")
# pollution_df.head()
# fig, ax = plt.subplots()

# # Scatter Plot
# ax.scatter(pollution_df["NO2 Mean"], pollution_df["O3 Mean"])
# fig, ax = plt.subplots()
# ax.scatter(pollution_df["NO2 Mean"], pollution_df["O3 Mean"])

# # Insert code here
# ax.set_title("NO2 and O3 Mean Measurements")
# ax.set_xlabel("NO2 Mean (parts per billion)")
# ax.set_ylabel("O3 Mean (parts per billion)")
# ax.grid(True)

# # Insert code here
# fig, ax = plt.subplots()
# # Box Plot
# ax.boxplot(pollution_df["O3 Mean"].dropna(), vert=False)

# # Insert code here
# ax.set_title("O3 Mean Box Plot")
# ax.set_xlabel("O3 Mean (parts per billion)")

# # fig, ax = plt.subplots()
# # ax.hist(retail_features_df["Fuel_Price"], bins=np.arange(2.5, 4.0, .1), edgecolor="black")

# # ax.set_title("Distribution of Fuel Price")
# # ax.set_xlabel("Fuel_Price (Dollars)")

# # fig, ax = plt.subplots()
# # ax.hist(retail_features_df["Unemployment"])

# # ax.set_title("Distribution of Unemployment Rate")
# # ax.set_xlabel("Unemployment Rate (Percent)")

# # fig, ax = plt.subplots()
# # ax.hist(retail_features_df["Unemployment"], edgecolor="black")

# # ax.set_title("Distribution of Unemployment Rate")
# # ax.set_xlabel("Unemployment Rate (Percent)")

# custom_bins = [3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9]
# custom_bins = np.arange(3.5, 9.5, .5)
# fig, ax = plt.subplots()
# # ax.hist(retail_features_df["Unemployment"], edgecolor="black", bins=custom_bins)

# ax.set_title("Distribution of Unemployment Rate")
# ax.set_xlabel("Unemployment Rate (Percent)")

# # print("Mean = " + str(np.mean(retail_features_df["Unemployment"])))
# # print("Mean - Stdev = " + str(np.mean(retail_features_df["Unemployment"])-np.std(retail_features_df["Unemployment"])))
# # print("Mean + Stdev = " + str(np.mean(retail_features_df["Unemployment"])+np.std(retail_features_df["Unemployment"])))

# fig, ax = plt.subplots()
# # ax.hist(retail_features_df["Unemployment"], edgecolor="black", bins=custom_bins)

# ax.set_title("Distribution of Unemployment Rate")
# ax.set_xlabel("Unemployment Rate (Percent)")

# # ax.axvline(np.mean(retail_features_df["Unemployment"]), color="red")
# # ax.axvline(np.mean(retail_features_df["Unemployment"])-np.std(retail_features_df["Unemployment"]), color="black")

# fig, ax = plt.subplots()
# # ax.hist(retail_features_df["Unemployment"], edgecolor="black", bins=custom_bins)

# ax.set_title("Distribution of Unemployment Rate")
# ax.set_xlabel("Unemployment Rate (Percent)")

# # ax.axvline(np.mean(retail_features_df["Unemployment"]), 
#         #    color="red", label="Mean")

# # ax.axvline(np.mean(retail_features_df["Unemployment"])-np.std(retail_features_df["Unemployment"]), 
#         #    color="black", label="+/- 1 Stdev")

# # ax.axvline(np.mean(retail_features_df["Unemployment"])+np.std(retail_features_df["Unemployment"]),
#         #    color="black")


# ig, ax = plt.subplots()
# # ax.boxplot(retail_features_df["Fuel_Price"], labels=[''], vert=False)

# ax.set_title("Distribution of Fuel Prices")
# ax.set_xlabel("Price in Dollars")

# fig, ax = plt.subplots()
# # ax.boxplot(retail_features_df["Unemployment"].dropna())

# ax.set_title("Distribution of Unemployment Rate")
# ax.set_xlabel("Unemployment Rate, percent")

# fig, ax = plt.subplots()
# # ax.boxplot(retail_features_df["Unemployment"].dropna(), vert=False)

# ax.set_title("Distribution of Unemployment Rate")
# ax.set_xlabel("Unemployment Rate, percent")

pollution_df = pd.read_csv('https://raw.githubusercontent.com/pathstream-curriculum/Python/master/pollution_ca_2012_2016.csv')
pollution_df.head()
fig, ax = plt.subplots()
ax.hist(pollution_df["O3 Mean"])

ax.set_title("O3 Mean Distribution")
ax.set_xlabel("O3 Mean (Parts per million)")
custom_bins = np.arange(0, 0.085, .005)

fig, ax = plt.subplots()
ax.hist(pollution_df["O3 Mean"], bins=custom_bins, edgecolor="black")

ax.set_title("O3 Mean Distribution")
ax.set_xlabel("O3 Mean (Parts per million)")

fig, ax = plt.subplots()
ax.hist(pollution_df["O3 Mean"], bins=custom_bins, edgecolor="black")

ax.set_title("O3 Mean Distribution")
ax.set_xlabel("O3 Mean (Parts per million)")
ax.axvline(np.mean(pollution_df["O3 Mean"]))

# Insert code here
fig, ax = plt.subplots()
ax.hist(pollution_df["O3 Mean"], bins=custom_bins, edgecolor="black")

ax.set_title("O3 Mean Distribution")
ax.set_xlabel("O3 Mean (Parts per million)")
ax.axvline(np.mean(pollution_df["O3 Mean"]), color="black", label="Mean")
ax.legend()

custom_bins2 = np.arange(0, 65, 5)
fig, ax = plt.subplots()
ax.hist(pollution_df["NO2 Mean"], edgecolor="black", bins=custom_bins2)

ax.set_title("Distribution of NO2 Mean")
ax.set_xlabel("NO2 Mean (parts per billion)")
ax.axvline(np.mean(pollution_df["NO2 Mean"]), color="red", label="Mean")
ax.axvline((np.mean(pollution_df["NO2 Mean"])-np.std(pollution_df["NO2 Mean"])), color="black", label="+/- 1 Stdev")
ax.axvline((np.mean(pollution_df["NO2 Mean"])+np.std(pollution_df["NO2 Mean"])), color="black")
ax.legend()

# Insert code here
fig, ax = plt.subplots()
ax.boxplot(pollution_df["O3 Mean"], vert=False)

ax.set_title("Distribution of O3 Mean")
ax.set_xlabel("O3 Mean(Parts Per Million)")
fig, ax = plt.subplots()
ax.boxplot(pollution_df["NO2 Mean"], vert=False)

ax.set_title("Distribution of NO2 Mean")
ax.set_xlabel("NO2 Mean(Parts Per Billion)")

# fig, ax = plt.subplots()
# ax.bar(average_fuel_price_by_location.index, average_fuel_price_by_location["Unemployment"])

# ax.set_xticklabels(labels=average_fuel_price_by_location.index)
# ax.set_title("Average Unemployment in each Store Location")
# ax.set_ylabel("Unemployment (Percentage)")
# fig, ax = plt.subplots()
# ax.bar(avg_temp_by_location.index, avg_temp_by_location["Temperature"])

# ax.set_title("Average Temperature in each Store Location")
# ax.set_ylabel("Temperature (Fahrenheit)")

def filter_df(store):
    filtered_df = retail_sales_df.loc[(retail_sales_df["Store"] == store) &
                                      (retail_sales_df["Dept"] == "Electronics") &
                                      (retail_sales_df["Year"] == 2010)]
    return filtered_df

# fig, ax = plt.subplots()
# ax.plot(seattle_df["Date"], seattle_df["Weekly_Sales"], label="Seattle")
# ax.plot(buffalo_df["Date"], buffalo_df["Weekly_Sales"], label="Buffalo")
# ax.plot(las_vegas_df["Date"], las_vegas_df["Weekly_Sales"], label="Las Vegas")
# ax.plot(los_angeles_df["Date"], los_angeles_df["Weekly_Sales"], label="Los Angeles")

# ax.set_ylabel("Weekly Sales ($)")
# ax.set_title("Weekly Electronics Sales for each Store Location")
# ax.legend()

city_agg_so2 = pollution_df.groupby("City").agg({"SO2 Mean": "mean"})
fig, ax = plt.subplots()
ax.bar(city_agg_so2.index, city_agg_so2["SO2 Mean"])

ax.set_title("Average SO2 by City")
ax.set_ylabel("Average SO2 (Parts Per Billion)")
city_agg_co = pollution_df.groupby("City").agg({"CO Mean": "mean"})

fig, ax = plt.subplots()
ax.bar(city_agg_co.index, city_agg_co["CO Mean"])

ax.set_title("Average CO by City")
ax.set_ylabel("Average CO (Parts Per Million)")

pollution_df["Date Local"] = pd.to_datetime(pollution_df["Date Local"])
pollution_df.info()
pollution_df.sort_values("Date Local", inplace=True)
fig, ax = plt.subplots()
ax.plot(pollution_df["Date Local"], pollution_df["SO2 Mean"])

ax.set_title("Change in SO2 Mean over time")
ax.set_ylabel("SO2 Mean (Parts Per Billion)")
ax.set_xlabel("Date")
pollution_df_2015 = pollution_df.loc[pollution_df["Date Local"].dt.year >= 2015]

fig, ax = plt.subplots()
ax.plot(pollution_df_2015["Date Local"], pollution_df_2015["SO2 Mean"])

ax.set_title("Change in SO2 Mean Over 2015 and 2016")
ax.set_ylabel("SO2 Mean (Parts Per Billion)")
ax.set_xlabel("Date")

pollution_df["Date Local"] = pd.to_datetime(pollution_df["Date Local"])
# Insert code here
pollution_df_bur = pollution_df.loc[(pollution_df["City"] == "Burbank") &
                                    (pollution_df["Date Local"].dt.year == 2013)]


fig, ax = plt.subplots()
ax.scatter(pollution_df_bur["CO Mean"], pollution_df_bur["NO2 Mean"])

ax.set_title("The Relationship Between CO and NO2")
ax.set_xlabel("CO Mean (Parts Per Million)")
ax.set_ylabel("NO2 Mean (Parts Per Billion)")

fig, ax = plt.subplots()
ax.scatter(pollution_df_bur["CO Mean"], pollution_df_bur["SO2 Mean"])

ax.set_title("The Relationship Between CO and SO2")
ax.set_xlabel("CO Mean (Parts Per Million)")
ax.set_ylabel("SO2 Mean (Parts Per Billion)")

fig, ax = plt.subplots()
ax.scatter(pollution_df_bur["CO Mean"], pollution_df_bur["O3 Mean"])

ax.set_title("The Relationship Between CO and O3")
ax.set_xlabel("CO Mean (Parts Per Million)")
ax.set_ylabel("O3 Mean (Parts Per Million)")