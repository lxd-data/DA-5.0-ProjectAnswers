import pandas as pd
avo_df = pd.read_csv("avocado.csv")

avo_df.head()
avo_df.tail()

avo_df.shape
avo_df.info()
avo_df.describe()
avo_df.value_counts()


avo_df['region'].value_counts()["Chicago"]
avo_df['AveragePrice'].mean()
chicago_avo_df = avo_df[avo_df["region"] == "Chicago"]
chicago_avo_df.shape
chicago_avo_df.reset_index()
avo_df['AveragePrice'].mean()
chicago_above_ave = chicago_avo_df[chicago_avo_df['AveragePrice'] > avo_df['AveragePrice'].mean()]


def filter_region_and_price(df, region, price):
    region_filter = df.loc[df["region"] == region]
    price_filter = region_filter.loc[region_filter["AveragePrice"] > price]
    final_df = price_filter.reset_index(drop=True)
    return final_df

charlotte_df = filter_region_and_price(avo_df, "Charlotte", mean_all)
ny = filter_region_and_price(avo_df, "NewYork", mean_all)
denver = filter_region_and_price(avo_df, "Denver", mean_all)
Indianapolis = filter_region_and_price(avo_df, "Indianapolis", mean_all)