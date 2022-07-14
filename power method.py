# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 12:20:09 2022

@author: mehar
"""

import sys
import numpy as np
from copy import deepcopy

# function to find the element with
# largest absolute value in an array(1-D)


def largElem(y, n):
    max = y[0]
    for i in range(n):
        if abs(y[i]) > abs(max):
            max = y[i]
    return max

# function to find eigen value,y


def powerMethod(A, n, x):
    y = np.zeros(n)  # variable to store next x values
    # finding each row of y ( A multiplied by x)
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += x[j]*A[i][j]
        y[i] = sum

    value = largElem(y, n)
    y /= value

    return y, value

# function to find inverse of a matrix using doolittle decomposition


def findInv(A, n):
    L = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                L[i][j] = 1

    # elimination
    U = A

    for k in range(n - 1):
        if U[k][k] == 0.0:
            print("cannot divide by zero ")
            sys.exit(400)
        else:
            for i in range(k + 1, n):
                factor = U[i][k] / U[k][k]
                for j in range(n):
                    U[i][j] = U[i][j] - factor * U[k][j]
                L[i][k] = factor

    # print(f"L =\n{L}\n\nU =\n{A}\n\n")

    INV = np.zeros((n, n))

    for t in range(n):

        # forward substitution
        D = np.zeros(n)
        b = np.zeros(n)

        b[t] = 1

        D[0] = b[0]

        for i in range(1, n):
            sum = 0
            for j in range(n):
                sum += L[i][j] * D[j]
            D[i] = b[i] - sum

        # Back Substitution
        X = np.zeros(n)

        X[n - 1] = D[n - 1] / U[n - 1, n - 1]

        for i in range(n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, n):
                sum += U[i][j] * X[j]
            X[i] = (D[i] - sum) / U[i][i]

        INV[:, t] = X
    return INV


'''<----------------------------------------------------------------------------------------------->'''

# initial values

A = np.array([[-30., 10., 20.], [10., 40., -50.], [20., -50., -10.]])
n = len(A)
# x=np.array([1.,1.,1.])
x = np.ones(n)  # array of given shape "n" filled with ones
max = 0
a=np.zeros((10,10))
a.shape
for i in range(10):
  for j in range(10):
    if i==j:
      a[i][j]=4
      if i+1<10:
        a[i+1][j]=2
      if j+1<10:
        a[i][j+1]=2
      if i+2<10:
        a[i+2][j]=1
      if j+2<10:
        a[i][j+2]=1
print(a)
m=len(a)

# error specified in %
err = 2.5e-6

condition = True
while condition:
    maxBefore = deepcopy(max)  # copying the value of max to maxBefore
    x, max = powerMethod(A, n, x)

    # calculating the error
    error = abs((max-maxBefore)*100/max)

    # if the error is non zero and is less than specified
    # error "err" then stop the loop , otherwise continue loop
    if error:
        if (error <= err):
            condition = False
            print("%.6f\nlargest eigen value = %.6f\n\n" % (max, max))
        else:
            print("%.6f" % max)
    else:
        print("%.6f" % max)
    # print(f"error = {error}")

'''<----------------------------------------------------------------------------------------------->'''
# calculating the inverse of matrix A
Ainv = findInv(A, n)

# initial values
# x=np.array([1.,1.,1.])
x = np.ones(n)  # array of given shape "n" filled with ones
min = 0

# error specified in %
err = 1.0e-5

condition = True
while condition:
    minBefore = deepcopy(min)  # copying the value of min to minBefore
    x, min = powerMethod(Ainv, n, x)

    # calculalting the error
    error = abs((min-minBefore)*100/min)

    # if the error is non zero and is less than specified
    # error "err" then stop the loop , otherwise continue loop
    if error:
        if (error <= err):
            condition = False
            print("%.6f\nsmallest eigen value = %.6f" % (1/min, 1/min))
        else:
            print("%.6f" % (1/min))
    else:
        print("%.6f" % (1 / min))
    # print(f"error2 = {error}")
    
    
