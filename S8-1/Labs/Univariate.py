# Import packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

avo_df = pd.read_csv("https://raw.githubusercontent.com/pathstream-curriculum/Python/master/avocado.csv")
avo_df.info()

avo_df.head()
avo_df['region'].value_counts()
total_us_df = avo_df[avo_df['region'] == 'TotalUS']
plt.hist(total_us_df['AveragePrice'], edgecolor='w')
plt.title('Distribution of Average Avocado Price across the US')
plt.xlabel('Price in Dollars')
custom_bins_1 = np.arange(.60, 2.2, step=.10)
custom_bins_2 = np.arange(.50, 2.25, step=.25)

plt.hist(total_us_df['AveragePrice'], edgecolor='w', bins= custom_bins_1)

plt.hist(total_us_df['AveragePrice'], edgecolor='w', bins= custom_bins_2)
plt.title('Distribution of Average Avocado Price across the US')
plt.xlabel('Price in Dollars')

total_us_conv = total_us_df[total_us_df['type'] == 'conventional']

# total_us_org contains only information about organic avocado sales. 
total_us_org = total_us_df[total_us_df['type'] == 'organic']

plt.hist(total_us_conv['AveragePrice'], edgecolor='w', bins= custom_bins_1)
plt.title('Distribution of Average Conventional Avocado Price across the US')
plt.xlabel('Price in Dollars')
plt.ylabel('Count')

plt.hist(total_us_org['AveragePrice'], edgecolor='w', bins= custom_bins_1)
plt.title('Distribution of Average Organic Avocado Price across the US')
plt.xlabel('Price in Dollars')
plt.ylabel('Count')

sf_conv = avo_df[(avo_df['type'] == 'conventional') & (avo_df['region'] == 'SanFrancisco')]
la_conv = avo_df[(avo_df['type'] == 'conventional') & (avo_df['region'] == 'LosAngeles')]
dfw_conv = avo_df[(avo_df['type'] == 'conventional') & (avo_df['region'] == 'DallasFtWorth')]


plt.boxplot(dfw_conv['Total Volume'], vert=False, labels=['San Francisco'])
plt.title("Total Volume of Avocados Sold in San Francisco")

plt.boxplot(dfw_conv['Total Volume'], vert=False, labels=['Los Angeles'])
plt.title("Total Volume of Avocados Sold in LA")

plt.boxplot(dfw_conv['Total Volume'], vert=False, labels=['Dallas Ft. Worth'])
plt.title("Total Volume of Avocados Sold in Dallas Ft. Worth")