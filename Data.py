import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

goals = pd.read_csv('goals_data.csv')
user_contract = pd.read_csv('User_contract_data.csv')

merged = pd.merge(goals, user_contract)

merged[['First_contract_Date', 'birth_date']] = merged[['First_contract_Date', 'birth_date']].apply(pd.to_datetime)
merged['AGE_GROUP'] = np.where(((pd.to_datetime('now') - merged['birth_date']) / np.timedelta64(1, 'Y')) > 30, 'Older than 30', 'Younger than 30')

#
# youngAndWon = merged[(merged.age <= 30) & (merged['STATUS'] == 'WON')]
# young = merged[merged.age <= 30]
# oldAndWon = merged[(merged.age > 30) & (merged['STATUS'] == 'WON')]
# old = merged[merged.age > 30]

###
# Total contracts amount per category by 2 group age (<= 30 and > 30)
###
table1 = merged.groupby(['CATEGORY', 'AGE_GROUP']).agg(amount_sum=("AMOUNT", 'sum'))
table1 = table1.reset_index()
plt.figure(figsize=(19, 15))
chart = sns.barplot(x="CATEGORY", y="amount_sum", hue='AGE_GROUP', data=table1)
chart.set(xlabel='Contract category', ylabel='Total contracts amount')
plt.legend(title='Age group')
plt.show()

###
# Total won contracts amount per category
###
table2 = merged.loc[merged['STATUS'] == 'WON']
table2 = table2.groupby(['CATEGORY']).agg(amount_sum=("AMOUNT", 'sum'))
table2 = table2.reset_index()

plt.figure(figsize=(19, 15))
chart = sns.barplot(x="CATEGORY", y="amount_sum", data=table2)
chart.set(xlabel='Contract category', ylabel='Total contracts amount')
plt.show()

###
# Total contracts amount per category by 2 group age (<= 30 and > 30) and gender
###
table3 = merged.loc[merged['STATUS'] == 'WON']
table3 = table3.groupby(['CATEGORY', 'AGE_GROUP']).agg(amount_sum=("AMOUNT", 'sum'))
table3 = table3.reset_index()

plt.figure(figsize=(19, 15))
chart = sns.barplot(x="CATEGORY", y="amount_sum", hue='AGE_GROUP', data=table3)
chart.set(xlabel='Contract category', ylabel='Total contracts amount')
plt.legend(title='Age group')
plt.show()

###
# Total contracts amount per category by 2 group age (<= 30 and > 30) and gender
###
table4 = merged.loc[merged['STATUS'] == 'WON']
table4.SESSO=table4.SESSO.fillna(table4.SESSO.mode()[0])
table4['SESSO'] = table4['SESSO'].map({'M': 1, 'F': 0})
table4 = table4.groupby(['CATEGORY', 'SESSO']).agg(amount_sum=("AMOUNT", 'sum'))
table4 = table4.reset_index()

plt.figure(figsize=(19, 15))
chart = sns.barplot(x="CATEGORY", y="amount_sum", hue='SESSO', data=table4)
chart.set(xlabel='Contract category', ylabel='Total contracts amount')
plt.legend(title='Gender')
plt.show()