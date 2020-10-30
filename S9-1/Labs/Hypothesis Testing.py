#!/usr/bin/env python
# coding: utf-8

# # Hypothesis Testing

# In[48]:


get_ipython().run_line_magic('autosave', '5')


# ## Task 1: Import packages and connect to data

# In[49]:


# Import libraries
from statsmodels.stats.weightstats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# In[50]:


# Connect to conventional avocado data
conv_avo_df = pd.read_csv("conventional_avo.csv")


# ## Task 2: Summer versus Winter Avocado Sales

# In[51]:


# Create three filtered DataFrames for TotalUS, SanDiego and Boston
conv_df_bos = conv_avo_df[conv_avo_df['region'] == 'Boston']
conv_df_sd = conv_avo_df[conv_avo_df['region'] == 'SanDiego']
conv_df_total_us = conv_avo_df[conv_avo_df['region'] == 'TotalUS']


# In[52]:


# Boxplot of TotalUS
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(data=conv_df_total_us, x="total_volume", y="summer", orient="h")
ax.set_title("Distribution of Total Volume of Avocados Sold, TotalUS region")


# In[53]:


# Boxplot of Boston 
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(data=conv_df_bos, x="total_volume", y="summer", orient="h")
ax.set_title("Distribution of Total Volume of Avocados Sold, Boston region")


# In[54]:


# Boxplot of SanDiego
fig, ax = plt.subplots(figsize=(10,5))
sns.boxplot(data=conv_df_sd, x="total_volume", y="summer", orient="h")
ax.set_title("Distribution of Total Volume of Avocados Sold, San Diego region")


# ## Task 3: Prepare Data for Testing 

# In[55]:


# Write a split_series function
def split_series(df):
    summer = df.loc[df["summer"]==True]["total_volume"]
    winter = df.loc[df["summer"]==False]["total_volume"]
    return summer, winter


# In[57]:


# Create two Series for each region
summer_total_us, winter_total_us = split_series(conv_df_total_us)
summer_sd, winter_sd = split_series(conv_df_sd)
summer_bos, winter_bos = split_series(conv_df_bos)


# ## Task 4: Run Summer and Winter t-tests

# In[58]:


# t-test for TotalUS
ttest_ind(summer_total_us, winter_total_us)


# In[59]:


# t-test for SanDiego
ttest_ind(summer_sd, winter_sd)


# In[60]:


# t-test for Boston 
ttest_ind(summer_bos, winter_bos)


# In[26]:


# Optional: play around with unequal variance


# ## Task 5: Comparing Proportions

# In[64]:


# Connect to SF/LA Data
avo_sf_la_2016 = pd.read_csv("avo_sf_la_2016.csv")
avo_sf_la_2016.tail()


# In[98]:


# Group and sum total volume of organic and conventional avocados by region
avo_sf_la_sums= avo_sf_la_2016.groupby("region").agg({
    "total_vol_org": "sum",
    "total_vol_conv": "sum"
})
avo_sf_la_sums


# In[99]:


# Create a column for total volume across both columns
avo_sf_la_sums['total_volume_all'] =     sum(avo_sf_la_sums[['total_vol_conv', 'total_vol_org']].loc['LosAngeles']),    sum(avo_sf_la_sums[['total_vol_conv', 'total_vol_org']].loc['SanFrancisco'])


# In[101]:


# Create a column for the proportion of organic to total volume
avo_sf_la_sums['proportion_org'] =     avo_sf_la_sums.loc['LosAngeles'][0]/avo_sf_la_sums.loc['LosAngeles'][1],    avo_sf_la_sums.loc['SanFrancisco'][0]/avo_sf_la_sums.loc['SanFrancisco'][1]


# ## Task 6: Perform a z-test

# In[31]:


# Store the necessary data under meaningful variable names for clarity


# Run a proportions z-test
proportions_ztest()
