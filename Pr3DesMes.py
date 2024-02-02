# Descriptive Statistics - Measures of Central Tendency and variability
# Perform the following operations on any open source dataset (e.g., data.csv)

# 1. Provide summary statistics (mean, median, minimum, maximum, standard deviation) for a
# dataset (age, income etc.) with numeric variables grouped by one of the qualitative (categorical) variable. For example, if your categorical variable is age groups and quantitative variable is income, then provide summary statistics of income grouped by the age groups. Create a list that contains a numeric value for each response to the categorical variable.

import pandas as pd

df=pd.read_csv('Salary_Data.csv')
df.head()
df.isnull()
df.isnull().sum()
df.dropna()
df.loc[df['Age']<=30,'categories']='Young age'
df.loc[(df['Age']>=31) & (df['Age']<=45),'categories']='Middle age'
df.loc[df['Age']>45,'categories']='Old Age age'
print(df)

med=df.groupby('categories')['Salary'].median()
print("\nMedian=",med)

mean=df.groupby('categories')['Salary'].mean()
print("\nMean=",mean)

mode=df.groupby('categories')['Salary'].agg(pd.Series.mode).to_frame()
print("\nMode=",mode)

des=df.groupby('categories')['Salary'].describe()
print("\nDescribe=",des)

# 2. Write a Python program to display some basic statistical details like percentile, mean, standard deviation etc. of the species of ‘Iris-setosa’, ‘Iris-versicolor’ and ‘Iris-versicolor’ of iris.csv dataset.

print("\n")
df=pd.read_csv('Iris.csv')
df.head()
df.isnull()
df.isnull().sum()
df.dropna()
print(df)

des=df.groupby('Species')['SepalLengthCm'].describe()
print("\nDescribe=",des)