import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score 
import joblib

# load dataset
data = pd.read_csv('data/data.csv', sep = '\t')

# first five rows of the dataset
print(data.head())

# shape of the dataser
print("\nshape of the dataset:")
print(data.shape)

# columns of the dataset
print("\ncolumns of the dataset:")
print(data.columns)

# info of the dataset
print("\ninfo about the dataset:")
print(data.info())

print("\nstatistical summary of the dataset:")
print(data.describe())

print('\nmissing values in the dataset:')
print(data.isnull().sum())

print("\nNumber of houses with price = 0:")
print((data['price']==0).sum())

# remove houses with price = 0
data = data[data['price']>0]
print("\nshape of the dataset after removing houses with price =0:")
print(data.shape)

# feature selection 

# target
y = data['price']
 
x = data.drop(['price','date','street','city','statezip','country'],axis=1)

#split dataset into traing and testing set
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2,random_state=42)

print("\nshape of x:",x.shape)

print("\nshape of y:",y.shape)

print("first five rows of x:\n",x.head())

print("first five rows of y:\n",y.head())

print("\ntraining features : ", x_train.shape)
print("\ntesting features : ", x_test.shape)

print("\ntraining Target : ", y_train.shape)
print("\ntesting Target : ", y_test.shape)

# create linear regressioin model
model = LinearRegression()

#model = RandomForestRegressor(n_estimators=300,max_depth=15 , min_samples_split=5,min_samples_leaf=2,random_state=42)

# train the model
model.fit(x_train,y_train)

print("\nmodel trained succesfully")

joblib.dump(model, 'model/house_price_model.pkl')
print("Model Saved Successfully!")

# prediction of the model
y_pred = model.predict(x_test)

print("\nfirst ten rows of predicted values:\n",y_pred[:10])


print("\nActual price vs predicted price:\n") 
for i in range(10):
    print(f"Actual price: {y_test.iloc[i]:,.2f} / predicted price: {y_pred[i]:,.2f}")

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test,y_pred)

print("\nmean squared error:",mse)
print("\nR2 score:",r2)