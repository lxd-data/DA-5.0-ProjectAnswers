retail_promo_df["Promo_Week"].value_counts()
fig = plt.figure()
sns.violinplot(data=retail_promo_df, x="Num_Visitors", y="Promo_Week", orient='h')
fig.suptitle("Number of Visitors per Week, Seattle")
retail_promo_df.groupby("Promo_Week").agg({"Num_Visitors": "mean"})

from statsmodels.stats.weightstats import ttest_ind
ttest_ind(dist_1, dist_2)


promo_weekly_sales = seattle_promos_df.loc[seattle_promos_df['Promo_Week']==True]['Num_Visitors']
non_promo_weekly_sales = seattle_promos_df.loc[seattle_promos_df['Promo_Week']==False]['Num_Visitors']

ttest_ind(promo_week_visitors, non_promo_week_visitors)

def check_pval(pval, sig_level):
    	if pval < sig_level:
		return "Reject the null hypothesis"
	else:
		return "Fail to reject the null hypothesis"

group_A_srs = df.loc[df["group"]=="A"]
group_B_srs = df.loc[df["group"]=="B"]

ttest_ind(group_A_srs, group_B_srs)

from statsmodels.stats.weightstats import ttest_ind
import statsmodels as sms

# You would then call the t-test function like this:
sms.stats.weightstats.ttest_ind(group1, group2)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.weightstats import ttest_ind

sns.set()

retail_promo_df = pd.read_csv('retail_promotions_seattle.csv')
retail_promo_df.head()

fig, ax = plt.subplots(figsize=(8,6))
sns.violinplot(data=retail_promo_df, x="Weekly_Sales", y="Promo_Week", orient='h')

ax.set_title("Weekly Sales Distribution, Seattle", size=20)
ax.set_ylabel("Promo_Week", size=15)
ax.set_xlabel("Weekly_Sales", size=15)

promo_wk_sales = retail_promo_df.loc[retail_promo_df["Promo_Week"]==True]["Weekly_Sales"]
non_promo_wk_sales = retail_promo_df.loc[retail_promo_df["Promo_Week"]==False]["Weekly_Sales"]
ttest_ind(promo_wk_sales, non_promo_wk_sales)


from statsmodels.stats.proportion import proportions_ztest
proportions_ztest([154, 191], [1000, 1000])

total_sales_and_visitors = retail_promo_df.groupby("Promo_Week").agg({"Num_Sales":"sum","Num-Visitors":"sum"})
total_sales_and_visitors

total_sales_and_visitors["proportion"] = total_sales_and_visitors["Num_Sales"] / total_sales_and_visitors["Num_Visitors"]
total_sales_and_visitors

proportions_ztest(total_sales_and_visitors["Num_Sales"], 
                  total_sales_and_visitors["Num_Visitors"])

# create a DataFrame with the total sales for the store, by date
sea_sales_df_all = sea_sales_df.groupby("Date").agg({"Weekly_Sales":"sum"}).reset_index()
#rename the Weekly_Sales columns to Weekly_Sales_all 
sea_sales_df_all.rename(columns={"Weekly_Sales": "Weekly_Sales_all"}, inplace=True) 

# create a DataFrame containing information about only the Housewares department
housewares_sales_df = sea_sales_df.loc[sea_sales_df["Dept"]=="Housewares"]
# rename the column to avoid confusion
housewares_sales_df.rename(columns={"Weekly_Sales": "Weekly_Sales_hw"}, inplace=True) 

housewares_join_all = housewares_sales_df.merge(sea_sales_df_all)[["Date", "Weekly_Sales_hw", "Weekly_Sales_all"]]

fig, ax = plt.subplots()
ax.scatter(housewares_join_all["Weekly_Sales_hw"], 
           housewares_join_all["Weekly_Sales_all"],
              s=50,
              alpha=0.5)
ax.set_xlim(70000, 130000)
ax.set_ylim(200000, 1000000)
ax.set_xlabel("Housewares Sales")
ax.set_ylabel("Total Store Sales")
ax.set_title("Weekly Seattle Store Sales")

from sklearn.linear_model import LinearRegression

lr_hw = LinearRegression()
housewares_join_all["Weekly_Sales_hw"].shape
housewares_join_all[["Weekly_Sales_hw"]].shape
x = housewares_join_all[["Weekly_Sales_hw"]]
y = housewares_join_all["Weekly_Sales_all"]
lr_hw.fit(x, y)
a, b = lr_hw.intercept_, lr_hw.coef_
a, b

my_df[["my_column_name"]]
x1 = 70000
y1 = a + b*x1
x2 = 130000
y2 = a + b*x2

fig, ax = plt.subplots()
ax.scatter(housewares_join_all["Weekly_Sales_hw"], 
           housewares_join_all["Weekly_Sales_all"],
              s=50,
              alpha=0.5)
ax.plot([x1, x2], [y1, y2], c='tab:red')
ax.set_xlim(70000, 130000)
ax.set_ylim(200000, 1000000)
ax.set_xlabel("Housewares Sales")
ax.set_ylabel("Total Store Sales")
ax.set_title("Weekly Seattle Store Sales")

electronics_sales_df = sea_sales_df.loc[sea_sales_df["Dept"]=="Electronics"]
electronics_sales_df.rename(columns={"Weekly_Sales": "Weekly_Sales_elec"}, inplace=True) 
electronics_join_all = electronics_sales_df.merge(sea_sales_df_all)[["Date", "Weekly_Sales_elec", "Weekly_Sales_all"]]

lr_elec = LinearRegression()
x = electronics_join_all[["Weekly_Sales"]]
y = electronics_join_all["Weekly_Sales_all"]
lr_elec.fit(x, y)
a, b = lr_elec.intercept_, lr_elec.coef_
a, b
x1 = 20000
y1 = a + b*x1
x2 = 180000
y2 = a + b*x2

fig, ax = plt.subplots()
ax.scatter(electronics_join_all["Weekly_Sales_elec"], 
           electronics_join_all["Weekly_Sales_all"],
              s=50,
              alpha=0.5)
ax.plot([x1, x2], [y1, y2], c='tab:red')
ax.set_xlim(20000, 180000)
ax.set_ylim(200000, 1000000)
ax.set_xlabel("Electronics Sales")
ax.set_ylabel("Total Store Sales")
ax.set_title("Weekly Seattle Store Sales")

from sklearn.metrics import mean_squared_error

mean_squared_error(measured_y_values, predicted_y_values)

sales_true = housewares_join_all["Weekly_Sales_all"]
sales_pred_hw = lr_hw.predict(housewares_join_all[["Weekly_Sales_hw"]])
mse_hw = mean_squared_error(sales_true, sales_pred_hw)
print("The RMSE for the housewares model is:", np.sqrt(mse_hw))

sales_true = electronics_join_all["Weekly_Sales_all"]
sales_pred_elec = lr_elec.predict(electronics_join_all[["Weekly_Sales_elec"]])
mse_elec = mean_squared_error(sales_true, sales_pred_elec)
print("The RMSE for the electronics model is:", np.sqrt(mse_elec))


# Insert code here
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

sns.set()

toys_join_all = pd.read_csv('store.csv')
toys_join_all.head()

fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(toys_join_all["Weekly_Sales_toys"], 
           toys_join_all["Weekly_Sales_all"], 
           s=100, 
           alpha=0.5)
ax.set_xlabel("Toys Sales", size=15)
ax.set_ylabel("Total Store Sales", size=15)
ax.set_title("Weekly Seattle Store Sales", size=20)

lr_toys = LinearRegression()
lr_toys.fit(toys_join_all[["Weekly_Sales_toys"]], toys_join_all["Weekly_Sales_all"])

a, b = lr_toys.intercept_, lr_toys.coef_

x1 = 5500
y1 = a + b*x1

x2 = 80000
y2 = a + b*x2

fig, ax = plt.subplots(figsize=(10,8))
ax.scatter(toys_join_all["Weekly_Sales_toys"], 
           toys_join_all["Weekly_Sales_all"],
              s=100,
              alpha=0.5)
ax.set_xlim(55000, 80000)
ax.set_ylim(200000, 1000000)
ax.set_xlabel("Toys Sales", size=15)
ax.set_ylabel("Total Store Sales", size=15)
ax.set_title("Weekly Seattle Store Sales", size=20)
ax.plot([x1, x2], [y1, y2], c='tab:red')

sales_true = toys_join_all["Weekly_Sales_all"]
sales_pred_toys = lr_toys.predict(toys_join_all[["Weekly_Sales_toys"]])
mse_toys = mean_squared_error(sales_true, sales_pred_toys)
print("The RMSE for the toys model is: ", np.sqrt(mse_toys))

