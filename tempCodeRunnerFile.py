sns.heatmap(corr,annot=True)
sns.histplot(df['fare'],kde=False,bins=10)