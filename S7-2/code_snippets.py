import pandas as pd 
import numpy as np

city = volunteers_df["city"].unique()

for i in city:
    print(i)
    new_df = volunteers_df[volunteers_df["city"] == i]
    print(new_df["age"].mean())

vehicles_df.groupby("type of vehicle")

volunteers_gb_city = volunteers_df.groupby("city")
volunteers_gb_city

volunteers_df.groupby("city").agg({"age" : "mean"})
vehicles_df.groupby("vehicle type").size()

volunteers_df.groupby("city").size()

df.groupby("column").size()

pizza_df.groupby("order_id").agg("sum")


volunteers_df.groupby("city").agg("mean")


volunteers_df.groupby("city").agg(["mean", "min", "max"])

volunteers_agg = volunteers_df.groupby("city").agg(["mean", "min", "max"])
volunteers_agg.columns

volunteers_agg[("hours", "min")]
volunteers_df.groupby("city").agg({"age" : "mean"})

volunteers_df.groupby("city").agg({"name" : "count",
                                   "age" : ["min", "max"],
                                   "hours" : ["mean", "std"]})

df.agg('mean')

df.agg('median')
volunteers_df.groupby("name")({"age" : ["mean", "median"]})

volunteers_df.groupby("name").agg({"age" : ["mean", "median"]})

volunteers_df.groupby().agg({"age" : ["mean", "median"]})
# volunteers_df.groupby("city").agg({"age" : "mean", "median"}) # syntax is incorrect but it is marked as an incorrect answer in the KC, so im assuming it was intentional



pollution_df = pd.read_csv("pollution_ca_2012_2016.csv")
pollution_df
pollution_df.groupby("County").mean()

pollution_df.groupby("City").agg({"NO2 Mean": "mean", 
                                  "O3 Mean": "mean", 
                                  "SO2 Mean": "mean", 
                                  "CO Mean": "mean"})

pollution_df.groupby("City").agg({"NO2 Mean": ["min", "max"]})
pollution_df.groupby("Date Local").size()

pollution_df.groupby("Date Local").agg({"CO Mean": ["min", "median", "max"],"NO2 Mean": ["min", "median", "max"]})

new_df = volunteers_df3["name", "age", "occupation", "hours", "city"]

pd.concat([user_df1, user_df2])
pd.concat([volunteers_df, volunteers_df2])
volunteers_df_joined.at[0, "name"]
array(['Tom', 'Marcus'], dtype=object)


volunteers_df_joined.at[7, "name"]
volunteers_df_joined.loc[0:2]

volunteers_df_joined = pd.concat([volunteers_df, volunteers_df2], ignore_index=True)
volunteers_df_joined

pd.concat[numbers_11to15, numbers_16to18]

pd.concat(numbers_11to15, numbers_16to18)

pd.concat([numbers_11to15 numbers_16to18])

pd.concat([numbers_11to15, numbers_16to18])




# Insert code here
pollution_df_la12 = pd.read_csv("pollution_la_2012.csv")
pollution_df_la12.head()

# Insert code here
pollution_df_la13 = pd.read_csv("pollution_la_2013.csv")
pollution_df_la13.head()

# Insert code here
pollution_df_la1213 = pd.concat([pollution_df_la12, pollution_df_la13], ignore_index=True)
pollution_df_la1213.info()

pollution_df_la1213.head()

# Insert code here
pollution_df_la1415 = pd.read_csv("pollution_la_2014_2015.csv")
pollution_df_la1415.head()

# Insert code here
pollution_df_la1215 = pd.concat([pollution_df_la1213, pollution_df_la1415], ignore_index=True)
pollution_df_la1215.info()
# Insert code here
pollution_df.head()

contact_df2 = contact_df.rename(columns={"first_name":"name"})


# Insert code here
pollution_df_la1216 = pd.read_csv("pollution_la_2012_2016.csv")
pollution_df_la1216.head()
# Insert code here
pollution_df_la1216.info()
# Insert code here
la_co_df = pd.read_csv("la_co_measurements.csv")
la_co_df.head()
# Insert code here
la_co_df.info()

# Insert code here
pollution_df_la_joined = pollution_df_la1216.merge(la_co_df)
pollution_df_la_joined.info()

# Insert code here
la_so2_df = pd.read_csv("la_so2_measurements.csv")
la_so2_df.head()
# Insert code here
la_so2_df.info()

# Insert code here
pollution_df_la_joined = pollution_df_la_joined.merge(la_so2_df)
pollution_df_la_joined.info()

# Insert code here
site_addresses_df = pd.read_csv("site_addresses.csv")
site_addresses_df.info()

# Insert code here
pollution_df_la_joined.merge(site_addresses_df)
pollution_df_la_joined.head()
# Insert code here
pollution_df_la_joined.info()