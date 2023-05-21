#! usr/local/bin/python3
# -*- coding : Utf-8 -*



import pandas as pd 
import numpy 
from numpy import exp, log, sum, dot
from scipy import optimize
from scipy.optimize import minimize
from fonctions.py import*


X = pd.read_excel('datatest.xlsx')
y = pd.read_excel('y.xlsx')
m = len(y)
initial_theta = numpy.zeros([8,1])
theta = numpy.zeros([8,1])

i=0
alpha = 0.01





theta = minimize(J, initial_theta, method='BFGS', options={'gtol':1e-05,'eps':1.5e-08} )

print(theta)

