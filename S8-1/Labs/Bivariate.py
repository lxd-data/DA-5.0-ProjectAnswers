#!/usr/bin/env python
# coding: utf-8

# # Task One

# In[34]:


get_ipython().run_line_magic('autosave', '5')


# In[35]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[36]:


avo_df = pd.read_csv("https://raw.githubusercontent.com/pathstream-curriculum/Python/master/avocado.csv")


# In[37]:


avo_df.info()


# In[38]:


print(avo_df.head())
print(avo_df.tail())


# In[39]:


avo_df.describe()


# In[40]:


# avo_df.columns = avo_df.columns.str.replace(" ", "_").str.lower() # this messed up some unit tests


# In[41]:


avo_df.Date = pd.to_datetime(avo_df.Date)
avo_df.Date


# In[42]:


avo_df_1 = avo_df[avo_df['region'].isin(["Albany", "Boston", "Charlotte", "Louisville", "Spokane"])]


# In[43]:


avo_df_1_agg = avo_df_1.groupby("region").agg({"Total Volume": "mean"})


# In[44]:


plt.bar(avo_df_1_agg.index, avo_df_1_agg['Total Volume'])
plt.title("Total Volume of Avocados Sold by City")
plt.ylabel("Total Volume Sold")


# # Task Three

# In[45]:


avo_df_2 = avo_df[avo_df['region'] == 'TotalUS']


# In[46]:


avo_df_2 = avo_df_2.sort_values(by= ['Date'], axis=0)


# In[47]:


avo_df_2_conv = avo_df_2[avo_df_2['type'] == 'conventional']


# In[48]:


# Create a line plot of Total Volume Sold Over Time
plt.plot(avo_df_2_conv["Date"], avo_df_2_conv['Total Volume'])
plt.xticks(rotation=45)
plt.title("Total Volume Sold Over Time")
plt.ylabel("Total Volume Sold")
plt.xlabel("Date")


# # Task Four

# In[49]:


avo_df_2_org = avo_df_2[avo_df_2['type'] == 'organic']


# In[52]:


# Lineplot that shows both organic and conventional sales over time
plt.plot(avo_df_2_conv["Date"], avo_df_2_conv['Total Volume'])
plt.plot(avo_df_2_org["Date"], avo_df_2_org['Total Volume'])
plt.xticks(rotation=45)
plt.title("Total Volume Sold Over Time")
plt.ylabel("Total Volume Sold")
plt.xlabel("Date")
plt.legend(["Conventional", "Organic"])


# # Task Five

# In[53]:


plt.scatter(avo_df_2_conv['AveragePrice'], avo_df_2_conv['Total Volume'])
plt.title("Conventional Avocado Average Price vs. Total Volume")
plt.xlabel("Average Price($)")
plt.ylabel("Total Volume Sold")


# In[54]:


plt.scatter(avo_df_2_org['AveragePrice'], avo_df_2_org['Total Volume'])
plt.title("Organic Avocado Average Price vs. Total Volume")
plt.xlabel("Average Price($)")
plt.ylabel("Total Volume Sold")


# # Task Six

# In[58]:


plt.scatter(avo_df_2_conv['AveragePrice'], np.log10(avo_df_2_conv['Total Volume']), s=50, alpha=0.3)
plt.scatter(avo_df_2_org['AveragePrice'], np.log10(avo_df_2_org['Total Volume']), s=50, alpha=0.3)
plt.title("Avocado Average Price vs. Total Volume")
plt.xlabel("Average Price($)")
plt.ylabel("Total Volume Sold")
plt.legend(["Conventional", "Organic"])


# In[ ]:




