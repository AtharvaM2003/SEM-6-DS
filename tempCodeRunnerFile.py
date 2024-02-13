
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset("titanic")
del df['deck']
mean = df['age'].mean()
df['age'].fillna(value=mean, inplace=True)
df.head()
print(df.isnull().sum())

# Plot 1
sns.distplot(x=df['age'], bins=10, kde=False)
plt.show()

# Plot 
sns.jointplot(x=df['age'], y=df['fare'], kind='scatter')
plt.show()

# Plot 3
sns.jointplot(x=df['age'], y=df['fare'], kind='hex')
plt.show()

# Plot 4
sns.rugplot(df['fare'])
plt.show()

# Plot 5
sns.barplot(x='sex', y='age', data=df, estimator=np.std)
plt.show()

# Plot 6
sns.countplot(x='sex', data=df)
plt.show()

# Plot 7
sns.boxplot(x='sex', y='age', data=df)
plt.show()

# Plot 8
sns.boxplot(x='sex', y='age', data=df, hue='survived')
plt.show()

# Plot 9
sns.violinplot(x='sex', y='age', data=df)
plt.show()

# Plot 10
sns.violinplot(x='sex', y='age', data=df, hue='survived')
plt.show()

# Plot 11
sns.stripplot(x='sex', y='age', data=df, jitter=False)
plt.show()

# Plot 12
sns.stripplot(x='sex', y='age', data=df)
plt.show()

# Plot 13
sns.stripplot(x='sex', y='age', data=df, jitter=True, hue='survived')
plt.show()

# Plot 14
sns.swarmplot(x='sex', y='age', data=df)
plt.show()

# Plot 15
sns.swarmplot(x='sex', y='age', data=df, hue='survived')
plt.show()

# Plot 16
sns.swarmplot(x='sex', y='age', data=df)
plt.show()

# Plot 17
df2 = df.drop(['sex', 'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive', 'alone'], axis=1)
df2 = df2.dropna()
corr = df2.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True)
plt.show()

# Plot 18
sns.histplot(df['fare'], kde=False, bins=10)
plt.show()

# Plot 19
plt.figure(figsize=(10, 8))
sns.clustermap(corr, annot=True)
plt.show()
