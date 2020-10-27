#!/usr/bin/env python
# coding: utf-8

# # 1. Titanic Analysis Summary

# In this analysis, we found that females were much more likely to survive than males, and we equated this discovery with the fact that females and young children were provided with vests and life boats first. We also discovered that those in the first class had a much higher likelihood of surviving, while those in the second and third class trailed behind with, respectively, survival rates of ~40% and ~20%. Finally, we analyzed the age of those who survived and did not survive in each class. Most distributions for those who did survive were bimodal around the ages of 20-30 and 0-10. This makes logical sense, given that children and some young females/males were likely encouraged to board lifeboats.

# # 2. Import Libraries

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


# # 3. Initial Exploration

# In[5]:


#load the passengers dataset
passengers_df = pd.read_csv("titanic_passengers.csv")
passengers_df.head()


# In[6]:


# View the column data types in the passengers DataFrame. 
passengers_df.info()


# In[7]:


#load the survived dataset
survived_df = pd.read_csv('survived.csv')
survived_df.head()


# In[8]:


# View the column data types in the survived DataFrame. 
survived_df.info()


# In[9]:


# Merge the passengers and survived DataFrames to create the titanic_df
titanic_df = pd.merge(passengers_df, survived_df, on="PassengerId")
titanic_df.head()


# In[10]:


# Convert all column headers to snake case
titanic_df.columns = [col.replace(" ", "_").lower() for col in titanic_df.columns]
titanic_df.head()


# # 4. Data Wrangling

# ### Survival Overview

# This section provides an overview of how many people did and did not survive the sinking of the Titanic.
# 
# 61.6% of passengers aboard the titanic did **not** survive, while the remaining 38.4% did. This means that, in all, a little over 1 out of every 3 people aboard the Titanic survived. In whole numbers, this means a little under 350 people survived, while approximately 550 did not.

# In[11]:


# Create a pie and bar chart to describe who survived and who died.
fig, axs = plt.subplots(1,2,figsize=(18,8))
# The pie chart shows the percentage of people who survived the titanic vs. those who did not.
titanic_df["survived"].value_counts().plot.pie(explode=[0,0.1],autopct="%1.1f%%",ax=axs[0], shadow=True)
axs[0].set_title("Titanic Survivors", size=20)
axs[0].set_ylabel("")

# The bar chart shows the count of those who survived vs. those who did not.
sns.countplot(x="survived", data=titanic_df, ax=axs[1])
axs[1].set_title("Titanic Survivors", size=20)


# 61.6% of passengers (roughly 570 people) did not survive, while 38.4% (roughly 325) did.

# ### Does Sex Affect Survival?

# This section provides an overview of the affect of sex on whether you survived or not.
# 
# Through our research, we determined that females had a much higher chance of surviving. Roughly 75% of the survivors were females. This makes sense given that females and children were encouraged to board lifeboats **first**. On the other hand, males were a little under 20% of the total survivor population. In the right-most plot, these facts are clearly presented: a little under 500 males died, while only a little over 100 survived. Additionally, roughly 225 females survives in contrast with roughly 75 dead.

# In[12]:


# Two bar charts were created to show how sex played a role in if you survived or did not.
fig, axs = plt.subplots(1,2,figsize=(18,8))
# The first bar chart shows the percentage from each sex that survived. If you were female you had a far better chance.
titanic_df[["sex", "survived"]].groupby(["sex"]).mean().plot.bar(ax=axs[0])
axs[0].set_title("Percentage of Suvivors by Sex", size=20)
axs[0].set_ylabel("Percentage of Survivors", size=15)
axs[0].set_xlabel("Sex", size=15)

# The second bar chart shows the count of survivors and non-survivors from each sex.
sns.countplot(x="sex", hue="survived", data=titanic_df, ax=axs[1])
axs[1].set_title("Sex: Survived vs Dead", size=20)
axs[1].set_ylabel("Count", size=15)
axs[1].set_xlabel("Sex", size=15)


# Females were roughly 75% likely to survive, in comparison with an around 20% likelihood for males. Around 225 females survived, while only a little over 100 males did.

# ### Does Ticket Class (pclass) Affect Survival?

# This section analyzes whether ticket class affects survival.
# 
# In this section, we discovered that the first ticket class had the largest percentage of survivors (63%), while the third class had the lower percentage (24%). The percentage of survival decreased as your class gets lower (1 $\rightarrow$ 2 and 2 $\rightarrow$ 3), which makes logical sense given that the third class was the lowest on the ship and the first was the highest and most privileged passengers.

# In[20]:


# This code cell contains DataFrame manipulations that were used to calculate percentages for the following bar chart.

# Groupby + agg function for pclass.
pclass_df = titanic_df.groupby("pclass").agg({"survived": ["count", "sum"]})
# Remove the "survived" level from the DataFrame column titles.
pclass_df.columns = pclass_df.columns.droplevel(0)
# Change the names of the columns to be more descriptive of what they show.
pclass_df.rename(columns={"count" : "total", "sum" : "survived"}, inplace=True)
# Create two new columns by calculating the percentages of those who survived and thos who did not.
pclass_df["percentage_survived"] = pclass_df["survived"]/pclass_df["total"]
pclass_df["percentage_not_surv"] = (pclass_df["total"] - pclass_df["survived"])/pclass_df["total"]
# This column will represent 100% of the passengers and will be used as the bars behind for those that survived.
pclass_df["100%"] = 1


# Final DataFrame
pclass_df


# In[21]:


# A bar chart that shows the percentage of survivors from each Ticket class(pclass)

fig, ax = plt.subplots(figsize=(10,10)) 
# By sticking 100% bars behind the survived bars you can show the percentage of people who died in the same chart.
ax.bar(pclass_df.index.astype(str), pclass_df["100%"], label="Not Sruvived")
ax.bar(pclass_df.index.astype(str), pclass_df["percentage_survived"], label="Survived")


ax.set_title("The Percentage of Survivors from each Ticket Class", size=20)
ax.set_ylabel("Percentage of Survivors", size = 15)
ax.set_xlabel("Ticket Classes", size=15)
ax.legend()


# First class ticketholders were over 60% likely to survive, while second class had around a 50% chance and third class only had an ~30% chance of living.

# ### Is Age a Factor with Either Sex or pclass when it comes to survival?

# In this section, we analyze whether age is a factor with sex or pclass for those who survived vs. those who did not. Overall, we discovered that if you were under the age of twenty, you were more likely to survive and if you were between the ages of 40-50 you were relatively equally likely to survive or die. Between 20 and 30, you were much more likely to die than to survive.

# In[17]:


#Create two histograms to show the age of survivors who survived and those who did not.

# Create custom bins for both histograms
cust_bin = np.arange(0,85,5)

fig, axs = plt.subplots(1,2,figsize=(20,10), sharey=True)
# Did not survive histogram
titanic_df[titanic_df['survived'] == 0].age.plot.hist(ax=axs[0], bins=cust_bin, edgecolor='white', color='darkred')
axs[0].axvline(np.mean(titanic_df[titanic_df['survived'] == 0].age), color="black")
axs[0].set_title("Did not Survive", size=20)
axs[0].set_ylabel("Count", size=15)
axs[0].set_xlabel("Age", size=15)

# Survived histogram
titanic_df[titanic_df['survived']==1].age.plot.hist(ax=axs[1], color='green', bins=cust_bin, edgecolor='white')
axs[1].axvline(np.mean(titanic_df[titanic_df['survived'] == 1].age), color="black")
axs[1].set_title("Survived", size=20)
axs[1].set_xlabel("Age", size=15)


# These subplots show the distribution of ages for those who did and did not survive. The distribution of ages for those who **did** survive is tightly clustered around the individuals below the age of ten and those between afes 15 and 35. The distribution of ages for those who **did not** survive is tightly clustered around ages 20-45, and is slightly skewed right.

# In[18]:


# Create a violin plot to show sex and age distributions for survivors and non-survivors
fig, ax = plt.subplots(figsize=(15,8))
sns.violinplot(x="sex",y="age", hue="survived", data=titanic_df, split=True)
ax.set_title('Sex and Age vs Survived', size=20)


# The distribution for males highlights that men aged around 20 years had the highest concentration of those who died. Similarly, the distribution of males who survived is highly concentrated around 25 and below the age of 10. The distribution for females highlights that females around the age of 20 had the highest concentration of individuals who died and survived. 

# In[16]:


# Create a violin plot to show pclass age distribution for survivors and non-survivors
fig, ax = plt.subplots(figsize=(15,8))
sns.violinplot(x="pclass",y="age", hue="survived", data=titanic_df, split=True)
ax.set_title('Pclass and Age vs Survived', size=20)


# The distribution of those in first class who did not survive is highly clustered around the ages of 45-55. The distribution of those in first class who did survive is clustered around the upper 30's, with a large density of survivors centered between the ages of 20 and 40. The distribution for those in the second class who did not survive is highly centered around the age of 25-30, while the distribution of those who did survive from the second class is centered on the age 30 and age 10 and below. This distribution is bimodal. The distribution for those who did not survive on the third class is centered around age 20 with a bit of a right skew, and the distribution for those who did survive is bimodal with the density focused on age 25 and age 10.

# In[ ]:




