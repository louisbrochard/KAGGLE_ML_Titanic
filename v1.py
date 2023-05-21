#! usr/local/bin/python3
# -*- coding : Utf-8 -*



import pandas as pd 
import numpy 
from numpy import exp, log, sum, dot



X = pd.read_excel('datatest.xlsx')
y = pd.read_excel('y.xlsx')
m = len(y)
theta = numpy.zeros([8,1])

i=0
alpha = 0.01

c1 = dot(-X , theta)

while i < 1500 : 
	J = (1/m)*sum(-y*log(1/(1+exp(c1)))-(1-y)*log(1-(1/(1+exp(c1)))))
	
	temp0 = theta[0] - alpha * (1/m)*sum(((1/(1+exp(c1)))-y))
	

	temp1 = theta[1] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['Pclass'])))
	

	temp2 = theta[2] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['Sex'])))
	

	temp3 = theta[3] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['Age'])))
	

	temp4 = theta[4] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['SibSp'])))
	

	temp5 = theta[5] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['Parch'])))
	

	temp6 = theta[6] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['Fare'])))
		

	temp7 = theta[7] - alpha * (1/m)*sum((((1/(1+exp(c1)))-y)*(X['Embarked'])))

	theta = numpy.array([[temp0],[temp1],[temp2],[temp3],[temp4],[temp5],[temp6],[temp7]], dtype = object)

	print(theta)

	if i%10 == 0 : 
		print(J)
	i +=1 

print (theta)
