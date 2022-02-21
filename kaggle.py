import pandas as pd
from sklearn.ensemble import  RandomForestRegressor
from sklearn.metrics import mean_absolute_error as mae
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

train_data = pd.read_csv("C:/Users/Fahad/Desktop/train.csv")
test_data = pd.read_csv("C:/Users/Fahad/Desktop/test.csv")
y = train_data['SalePrice'] #target to be fitted in the model
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

X = train_data[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

model = DecisionTreeRegressor(max_leaf_nodes=250,random_state=1)

model.fit(train_X,train_y)

prediction = model.predict(val_X)
print(mae(val_y,prediction))

testData = test_data[features]

output_prediction = model.predict(testData)
finalOutPut = pd.DataFrame({'id': test_data['Id'] , 'SalePrice': output_prediction})
#finalOutPut.to_csv("kaggleSubmission.csv" , index = False)