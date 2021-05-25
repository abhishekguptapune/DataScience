#Label Encoding or Ordinal Encoding
import category_encoders as ce
import pandas as pd
train_df=pd.DataFrame({'Degree':
	 					['High school','Masters','Diploma','Bachelors','Bachelors','Masters','Phd','High school','High school']
	 					})

#Original data
train_df
print(train_df)

# create object of Ordinalencoding
encoder= ce.OrdinalEncoder(cols=['Degree'],return_df=True,
                           mapping=[{'col':'Degree',
'mapping':{'None':0,'High school':1,'Diploma':2,'Bachelors':3,'Masters':4,'Phd':5}}])

#fit and transform train data 
df_train_transformed = encoder.fit_transform(train_df)
print(df_train_transformed)