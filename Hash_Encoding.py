import category_encoders as ce
import pandas as pd

#Create the dataframe
data=pd.DataFrame({'Month':['January','April','March','April','Februay','June','July','June','September']})
print(data)

#Create object for hash encoder
encoder=ce.HashingEncoder(cols='Month',n_components=6)

#Fit and Transform Data
data_encoded = encoder.fit_transform(data)
print(data_encoded)