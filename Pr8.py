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
plt.title('Distribution of Age')
plt.show()

# Plot 2

sns.jointplot(x=df['age'], y=df['fare'], kind='scatter')
plt.title('Scatter Plot: Age vs Fare')
plt.show()

# Plot 3

sns.jointplot(x=df['age'], y=df['fare'], kind='hex')
plt.title('Hexbin Plot: Age vs Fare')
plt.show()

# Plot 4

sns.rugplot(df['fare'])
plt.title('Rug Plot: Fare')
plt.show()

# Plot 5

sns.barplot(x='sex', y='age', data=df, estimator=np.std)
plt.title('Bar Plot: Age by Sex (std)')
plt.show()

# Plot 6

sns.countplot(x='sex', data=df)
plt.title('Count Plot: Sex')
plt.show()

# Plot 7

sns.boxplot(x='sex', y='age', data=df)
plt.title('Box Plot: Age by Sex')
plt.show()

# Plot 8

sns.boxplot(x='sex', y='age', data=df, hue='survived')
plt.title('Box Plot: Age by Sex with Survival')
plt.show()

# Plot 9

sns.violinplot(x='sex', y='age', data=df)
plt.title('Violin Plot: Age by Sex')
plt.show()

# Plot 10

sns.violinplot(x='sex', y='age', data=df, hue='survived')
plt.title('Violin Plot: Age by Sex with Survival')
plt.show()

# Plot 11

sns.stripplot(x='sex', y='age', data=df, jitter=False)
plt.title('Strip Plot: Age by Sex (No Jitter)')
plt.show()

# Plot 12

sns.stripplot(x='sex', y='age', data=df)
plt.title('Strip Plot: Age by Sex (Jitter)')
plt.show()

# Plot 13

sns.stripplot(x='sex', y='age', data=df, jitter=True, hue='survived')
plt.title('Strip Plot: Age by Sex with Survival')
plt.show()

# Plot 14

sns.swarmplot(x='sex', y='age', data=df)
plt.title('Swarm Plot: Age by Sex')
plt.show()

# Plot 15

sns.swarmplot(x='sex', y='age', data=df, hue='survived')
plt.title('Swarm Plot: Age by Sex with Survival')
plt.show()

# Plot 16

sns.swarmplot(x='sex', y='age', data=df)
plt.title('Swarm Plot: Age by Sex')
plt.show()

# Plot 17
df2 = df.drop(['sex', 'embarked', 'class', 'who', 'adult_male', 'embark_town', 'alive', 'alone'], axis=1)
df2 = df2.dropna()
corr = df2.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True)
plt.title('Correlation Heatmap')
plt.show()

# Plot 18

sns.histplot(df['fare'], kde=False, bins=10)
plt.title('Histogram: Fare')
plt.show()

# Plot 19
plt.figure(figsize=(10, 8))
sns.clustermap(corr, annot=True)
plt.title('Cluster Map: Correlation')
plt.show()
