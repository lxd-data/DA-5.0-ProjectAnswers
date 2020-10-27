#!/usr/bin/env python
# coding: utf-8

# # Summary/Notes
# 
# ### When you have finished your data visualization exploration, return to this markdown cell and fill it out in preparation for your meeting with the analytics manager, Victor.
# 
# **Hypothesis 1 findings:** 
# 
# **Hypothesis 2 findings:**
# 
# **Hypothesis 3 findings:**
# 
# 

# # How to Complete This Notebook
# 
# This notebook has a skeleton structure to guide your exploration and keep you on track. More details about each task can be found in the project sidebar. Be sure to read the sidebar instructions for each step before writing your code. 

# # 1. IMPORT & EXPLORE THE DATA
# 
# ## 1A. Import Packages & Set Style

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set()


# ## 1B. Import the Data
# The datsets are stored in the following files:
# * "customers.csv"
# * "churn.csv"
# 
# These files are in the same folder you are currently working in. 

# In[3]:


customers = pd.read_csv("customers.csv")


# In[4]:


churn = pd.read_csv("churn.csv")


# ## 1C. Explore Your Data & Identify Structure
# Add as many code cells as you need to thoroughly explore both DataFrames here.

# In[5]:


churn.info()
churn.head(15)


# In[6]:


customers.info()
customers.head(15)


# # 2. VISUALIZE THE CUSTOMER DATA
# 
# ## 2A. Identify Columns Connected to Churn

# In[7]:


customer_subset = customers[["customer_id", "age", "gender", "number_of_referrals", "offer", "monthly_charge", "total_charges", "contract", "payment_method", "under_30", "senior_citizen", "married"]]


# ## 2B. Visualize the Data
# 
# ### Plot 1:

# In[8]:


gender_dict = dict(customer_subset.gender.value_counts())
x_labels = gender_dict.keys()
y_labels = gender_dict.values()
plt.bar(x_labels, y_labels)
plt.xlabel("Gender")
plt.ylabel("Frequency")
plt.title("Gender Breakdown in the Customer CSV")


# **Plot description:** 
# The ratio between male and females is almost equal. There are 3554 males and 3488 females

# ### Plot 2:

# In[9]:


age_dict = dict(customer_subset.age.value_counts())
print(age_dict)
print(min(age_dict.values()))
print(min(age_dict.keys()))
print(max(age_dict.keys()))
print(max(age_dict.values()))
x_labels = age_dict.keys()
y_labels = age_dict.values()
plt.bar(x_labels, y_labels)
plt.xlabel("Ages")
plt.ylabel("Frequency")
plt.title("Age Breakdown in the Customer CSV")


# **Plot description:** The ages included in the CSV are widely dispersed, with the most popular age being 42 and the least popular age being 72. The youngest age in the CSV is 19, and the oldest is 80.

# ### adding a few more plots...

# In[25]:


sns.boxplot(
    x="offer",
    y="total_charges",
    hue="offer",
    data= customer_subset
)


# ### boxplot
# 
# Offer E is the cheapest, with total charges around $1500$. Offer A is the most expensive, with total charges reaching past $8000$!

# In[27]:


sns.boxplot(
    x="offer",
    y="total_charges",
    hue="gender",
    data= customer_subset
)


# ### grouped boxplot
# This boxplot compares total charges vs. the available offers, and the boxplot is grouped by gender. Overall, it seems like men and women pay very comparable rates. In Offer E, B, and A, females pay a bit more, and in C males pay more than females in total charges. In offer D, the results are nearly exact.

# In[31]:


sns.displot(
    customer_subset, x="monthly_charge", col="offer", row="gender",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)


# ### Distplot
# This plot provides a more granular overview of what males and females are paying on a monthly basis. The columns are grouped by Offers, and the rows are grouped by Gender. It is interesting that, at each offer level, both males and females tend to pay the lowest monthly charge.

# <font color="red">adding a few more plots...</font>

# In[35]:


sns.displot(
    customer_subset, x="monthly_charge", col="contract", row="gender",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)


# In[51]:


sns.displot(
    customer_subset, x="monthly_charge", col="contract", row="senior_citizen",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
)


# In[57]:


sns.displot(
    customer_subset, x="payment_method", col="contract", row="senior_citizen",
    binwidth=10, height=5, facet_kws=dict(margin_titles=True),
)


# # 3. JOIN THE DATAFRAMES

# In[60]:


churn.customer_id = churn.customer_id.apply(lambda id_num: "".join(id_num.split("-")))
merged_df = pd.merge(customer_subset, churn, how='inner')


# # 4. EXPLORE CHURN HYPOTHESES

# ### 1. Question: Do younger customers churn at a higher rate?
# **Hypothesis:** Younger customers are always looking for new technology and better deals, while older customers might be less inclined to switch companies from what they are familiar with.

# In[79]:


merged_df["churn_label"].value_counts()

sns.boxplot(
    x="churn_label",
    y="age",
    data=merged_df
)


# **Plot Description:** The median age of people with a churn label of 'Yes' is 50 and the max is 65, while the median age of people with a churn label of 'No' is around 45 with a max.

# In[82]:


sns.displot(
    merged_df[merged_df["churn_label"] == "No"],
    x="age",
    hue="senior_citizen"
)


# In[83]:


sns.displot(
    merged_df[merged_df["churn_label"] == "Yes"],
    x="age",
    hue="senior_citizen"
)


# **Plot Description:** These two plots compare the frequency of the ages of people whose churn labels were "Yes" and "No". Interestingly, senior citizens are slightly more likely to churn than not (there is ~140 count for 65-80 year olds with 'Yes', in comparison with ~125 for 'No'). Alternatively, non-senior citizens are much more likely to not churn (except for age 50 and 60, the frequency of those with a churn label of "No" is greater than 250.

# ### 2. Question: -- create your own --
# **Hypothesis:** 

# In[ ]:





# **Plot Description:**

# In[ ]:





# **Plot Description:**

# ### 3. Question: -- create your own --
# **Hypothesis:**

# In[ ]:





# **Plot Description:**

# In[ ]:





# **Plot Description:**
