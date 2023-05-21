#! /usr/local/bin/python3
#-*- coding : utf-8 -*

import sklearn
from sklearn.tree import DecisionTreeRegressor
import pandas as pd 

print('The program starts... Loading...')

X = pd.read_excel('datatest.xlsx')
y = pd.read_excel('y.xlsx')

model = DecisionTreeRegressor(random_state = 1)

model.fit(X,y)

test = pd.read_excel('test.xlsx')
test = test.dropna(axis=0)

predictions = model.predict(test)

print(predictions)

ident = pd.read_excel('OutputID.xlsx')

output = pd.DataFrame({'PassengerId' : ident.PassengerId , 'Survived' : predictions})
output.to_csv('submission290820v2.csv', index=False)

