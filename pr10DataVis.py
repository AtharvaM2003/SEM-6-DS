import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("Iris.csv")
del df['Id']
sns.histplot(df['SepalLengthCm'],kde=False,bins=10)
plt.show()
sns.histplot(df['SepalWidthCm'],kde=False,bins=10)
plt.show()
sns.histplot(df['PetalLengthCm'],kde=False,bins=10)
plt.show()
sns.histplot(df['PetalWidthCm'],kde=False,bins=10)
plt.show()

sns.histplot(df['SepalLengthCm'],kde=True,bins=10)
plt.show()
sns.histplot(df['SepalWidthCm'],kde=True,bins=10)
plt.show()
sns.histplot(df['PetalLengthCm'],kde=True,bins=10)
plt.show()
sns.histplot(df['PetalWidthCm'],kde=True,bins=10)
plt.show()

sns.scatterplot(df['SepalLengthCm'])
plt.show()
sns.scatterplot(df['SepalWidthCm'])
plt.show()
sns.scatterplot(df['PetalLengthCm'])
plt.show()
sns.scatterplot(df['PetalWidthCm'])
plt.show()

sns.boxplot(x='Species', y='SepalLengthCm', data=df)
plt.show()
sns.boxplot(x='Species', y='SepalWidthCm', data=df)
plt.show()
sns.boxplot(x='Species', y='PetalLengthCm', data=df)
plt.show()
sns.boxplot(x='Species', y='PetalWidthCm', data=df)
plt.show()

sns.pairplot(df,hue='Species')
plt.show()