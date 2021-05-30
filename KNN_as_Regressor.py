# importing required libraries
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor

path = "iris.data"

#we need to assign column names to the dataset as follows
headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

#we need to read dataset to pandas dataframe as follows −
data = pd.read_csv(path, names = headernames)
array = data.values
X = array[:,:2]
Y = array[:,2]
print(data.shape)
print(Yz)

#Next, import KNeighborsRegressor from sklearn to fit the model −
knnr = KNeighborsRegressor(n_neighbors = 10)
knnr.fit(X, Y)

#At last, we can find the MSE as follows −
print ("The MSE is:",format(np.power(Y-knnr.predict(X),2).mean()))

#OUTPUT
#The MSE is: 0.12226666666666669
