import category_encoders as ce
import pandas as pd
data=pd.DataFrame({'City':[
'Delhi','Mumbai','Hydrabad','Chennai','Bangalore','Delhi','Hydrabad','Bangalore','Delhi'
]})

#Original Data
print(data)

encoder=ce.sum_coding.SumEncoder(cols='City',verbose=False,)

data_encoded = encoder.fit_transform(data)
print(data_encoded)