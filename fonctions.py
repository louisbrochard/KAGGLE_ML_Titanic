#! usr/local/bin/python3
# -*- coding : Utf-8 -*


import pandas as pd 
import numpy 
from numpy import exp, log, sum, dot
from scipy import optimize
from scipy.optimize import minimize


def J(theta):
	return J = (1/m)*sum(-y*log(1/(1+exp(dot(-X , theta))))-(1-y)*log(1-(1/(1+exp(dot(-X , theta))))))
