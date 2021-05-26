#import the libraries
import pandas as pd
import category_encoders as ce

#Create the Dataframe
data=pd.DataFrame({'class':['A','B','C','B','C','A','A','A'],'Marks':[50,30,70,80,45,97,80,68]})

#Original Data
print(data)

#Create target encoding object
encoder=ce.TargetEncoder(cols='class') 

#Fit and Transform Train Data
data_encoded = encoder.fit_transform(data['class'],data['Marks'])
print(data_encoded)