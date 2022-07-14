#!/usr/bin/env python
# coding: utf-8

# In[10]:


from sys import exit
import numpy as np


a = np.array([[3.0, -0.1, 0.2], [0.1, 7., -0.3], [0.3, -.2, 10.]])
b = ([7.85, -19.3, 71.4])
n=len(a)
def GaussJordanPartialPivot(a,b):

    if np.linalg.det(a) == 0:
        print("determinant is zero , no solution")
        exit(10)

    for k in range(n):
        if np.fabs(a[k][k]) < 1.0e-3:
            for i in range(k + 1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    for j in range(k, n):
                        a[k, j], a[i, j] = a[i, j], a[k, j]
                    b[i], b[k] = b[k], b[i]
                    break

        pivot = a[k, k]
        if pivot:
            for j in range(k, n):
                a[k, j] = a[k, j] / pivot
        else:
            print("cannot divide by zero")
            exit(20)
        b[k] = b[k] / pivot

        for i in range(n):
            if i == k or a[i][k] == 0:
                continue
            fact = a[i, k]
            for j in range(k, n):
                a[i, j] -= a[k, j] * fact
            b[i] -= b[k] * fact
    return b




if np.linalg.det(a) == 0:
    print("determinant is zero , no solution")
    exit(10)

for k in range(n):
    if np.fabs(a[k][k]) < 1.0e-3:
        for i in range(k + 1, n):
            if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                for j in range(k, n):
                    a[k, j], a[i, j] = a[i, j], a[k, j]
                b[i], b[k] = b[k], b[i]
                break

    pivot = a[k, k]
    if pivot:
        for j in range(k, n):
            a[k, j] = a[k, j] / pivot
    else:
        print("cannot divide by zero")
        exit(20)
    b[k] = b[k] / pivot

    for i in range(n):
        if i == k or a[i][k] == 0:
            continue
        fact = a[i, k]
        for j in range(k, n):
            a[i, j] -= a[k, j] * fact
        b[i] -= b[k] * fact


for i in range(n):
    print(%0.2f 'x{i + 1} = {b[i]}')


# In[ ]:





# In[ ]:





# In[ ]:




