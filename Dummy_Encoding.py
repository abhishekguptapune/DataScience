import category_encoders as ce
import pandas as pd
data=pd.DataFrame({'City':[
'Delhi','Mumbai','Hydrabad','Chennai','Bangalore','Delhi','Hydrabad','Bangalore','Delhi'
]})

#Original Data
print(data)

#encode the data
data_encoded=pd.get_dummies(data=data,drop_first=True)
print(data_encoded)