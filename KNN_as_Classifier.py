# importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

path = "iris.data"

#we need to assign column names to the dataset as follows
headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

#we need to read dataset to pandas dataframe as follows −
dataset = pd.read_csv(path, names = headernames)
print(dataset.head())

#Data Preprocessing will be done with the help of following script lines.
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Next, we will divide the data into train and test split. Following code will split the dataset into 60% training data and 40% of testing data −
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40)

#Next, data scaling will be done as follows −
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

#Next, train the model with the help of KNeighborsClassifier class of sklearn as follows −
classifier = KNeighborsClassifier(n_neighbors = 8)
classifier.fit(X_train, y_train)

#At last we need to make prediction. It can be done with the help of following script −
y_pred = classifier.predict(X_test)

result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)
result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)

error = []

# Calculating error for K values between 1 and 40
for i in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    error.append(np.mean(pred_i != y_test))
print(error)
plt.figure(figsize=(12, 6))
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')
plt.xlabel('K Value')
plt.ylabel('Mean Error')
plt.show()