import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
df=pd.read_csv("Iris.csv")
del df['Id']


# sns.histplot(df['SepalLengthCm'],kde=False,bins=10)
# plt.show();
# sns.histplot(df['SepalWidthCm'],kde=False,bins=10)
# plt.show();
# sns.histplot(df['PetalLengthCm'],kde=False,bins=10)
# plt.show();
# sns.histplot(df['PetalWidthCm'],kde=False,bins=10)
# plt.show();

# sns.boxplot(x='Species', y='SepalLengthCm', data=df)
# plt.show()
# sns.boxplot(x='Species', y='SepalWidthCm', data=df)
# plt.show()
# sns.boxplot(x='Species', y='PetalLengthCm', data=df)
# plt.show()
# sns.boxplot(x='Species', y='PetalWidthCm', data=df)
# plt.show()

sns.scatterplot(x='Species', y='SepalLengthCm', data=df)
plt.show()
sns.scatterplot(x='Species', y='SepalWidthCm', data=df)
plt.show()
sns.scatterplot(x='Species', y='PetalLengthCm', data=df)
plt.show()
sns.scatterplot(x='Species', y='PetalWidthCm', data=df)
plt.show()