# 1. Implement Simple Naïve Bayes classification algorithm using Python/R on iris.csv dataset.
# 2. Compute Confusion matrix to find TP, FP, TN, FN, Accuracy, Error rate, Precision, Recall on the given dataset.
import pandas as pd
df=pd.read_csv('Salary_Data.csv')
df=df.dropna()
X=df
Y=df
X=X.drop(['Gender','Education Level','Job Title',],axis=1)
print("X=",X)
Y=Y.drop(['Age','Gender','Job Title','Years of Experience','Salary'],axis=1)
print("Y=",Y)


from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2,random_state=40)
print("\nX_train",X_train)
print("\nX_test",X_test)
print("\nY_test",Y_test)
print("\nY_train",Y_train)

from sklearn.naive_bayes import GaussianNB

classifier=GaussianNB()
classifier.fit(X_train,Y_train)
prediction=classifier.predict(X_test)
print("\nPrediction:",prediction)

from sklearn.metrics import confusion_matrix,accuracy_score,precision_score,recall_score

cm=confusion_matrix(prediction,Y_test)
ac=accuracy_score(Y_test,prediction)
ps=precision_score(Y_test,prediction,average='weighted')
rs=recall_score(Y_test,prediction,average='weighted')
print("\nConfusion Matrix:\n",cm)
print("\nAccuracy:",ac)
print("\nPrecision:",ps)
print("\nRecall Value:",rs)
