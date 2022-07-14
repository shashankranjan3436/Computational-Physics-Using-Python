#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import numpy as np
from numpy import array, zeros, fabs



n = int(input('Enter number of unknowns: '))
a = np.zeros((n,n))
b = np.zeros(n)
x = np.zeros(n)
print('Enter Augmented Matrix Coefficients:')
for i in range(n):
    for j in range(n):
        a[i][j] = float(input( 'a['+str(i)+']['+ str(j)+']='))
    b[i] =float(input( 'b['+str(i)+']=')) 

n = len(b)
x = zeros(n, float)

for k in range(1,n):
    t=a[k-1][k-1]
    for j in range(k+1,n+1):
        if a[j-1][k-1]>t:
            t=j
    for i in range(k,n+1):
        temp=a[k-1][i-1]
        a[k-1][i-1]=a[t-1][i-1]
        a[t-1][i-1]=temp
    temp=b[k-1]
    b[k-1]=b[t-1]
    b[t-1]=temp
    
    
for i in range(k+1,n):
        factor = a[k,k]/a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j]*factor
        b[i] = b[k] - b[i]*factor
print(a)
print(b)


x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0
  
    for j in range(i+1, n):
        sum_ax += a[i,j] * x[j]
        
    x[i] = (b[i] - sum_ax) / a[i,i]

print("The solution of the system is:")
print(x)


# In[ ]:





# In[ ]:




