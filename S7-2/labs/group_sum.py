import pandas as pd

import pandas as pd

avo_df = pd.read_csv("avocado.csv")
#avo_df["Date"] = pd.to_datetime(avo_df.Date)
avo_df.head()

avo_df_2017_conv = avo_df[(avo_df['year'] == 2017) & (avo_df['type']=='conventional')]
avo_df_2017_conv

regional_gb = avo_df_2017_conv.groupby("region")
sum_total_vol_by_region = regional_gb.agg({"Total Volume": "sum"})
sum_total_vol_by_region.columns

sum_total_vol_by_region.sort_values('Total Volume', ascending=False)

average_price_stats = regional_gb.agg({"AveragePrice" : ['mean','min','max']})
average_price_stats.columns

average_price_stats.sort_values(('AveragePrice', 'mean'))

average_price_stats[("AveragePrice", "min")].argmax()
average_price_stats[("AveragePrice", "max")].argmax()
average_price_stats.iloc[49]
average_price_stats.iloc[average_price_stats[("AveragePrice", "max")].argmax()]
