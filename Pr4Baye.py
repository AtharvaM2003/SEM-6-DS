# 1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv dataset.
# 2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall on the given dataset.
import pandas as pd
df=pd.read_csv('Iris.csv')
X=df
Y=df
X=X.drop(['Species','Id'],axis=1)
print("X=",X)
Y=Y.drop(['SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm','Id'],axis=1)
print("Y=",Y)

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
print(X_train)
