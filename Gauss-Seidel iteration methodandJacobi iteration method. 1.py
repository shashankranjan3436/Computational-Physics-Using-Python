
import numpy as np
x = [0, 0, 0]                        
a = [[3, 7, 13],[1, 5, 3],[12, 3, -5]]
b = [76,28,1]
n = len(a)


#to check whethergiven matrix is diagonally dominant or not
def isDDM(m, n) :
 
    # for each row
    for i in range(0, n) :        
     
        # for each column, finding
        # sum of each row.
        sum = 0
        for j in range(0, n) :
            sum = sum + abs(m[i][j])    
 
        # removing the
        # diagonal element.
        sum = sum - abs(m[i][i])
 
        # checking if diagonal
        # element is less than
        # sum of non-diagonal
        # element.
        if (abs(m[i][i]) < sum) :
            return False
 
    return True
 
# Driver Code

 
if((isDDM(a, n))) :
    print ("True")
else :
    print ("False")

print
def seidel(a, x, b):
    n = len(a)    #for loop for 3 times calculation
    for j in range(0, n):
        d = b[j]  #temp variable to store d
        for i in range(0, n):
            if(j!=i):
                d -= a[j][i] * x[i]
        x[j] = d / a[j][j]   # returning updated solution
    return np.round(x, 7)


print('seidel iteration')
for i in range(0, 15):    # loop run for 15 iterations
    x = seidel(a, x, b)
    print('\niteration'+str(i+1),str(x),sep='\t')
    
    
def jacobi(a, x, b):
    n = len(a)
    y =[0,0,0]  #for loop for 3 times calculation
    for j in range(0, n):
        d = b[j]  #temp variable to store d
        for i in range(0, n):
            if(j != i):
                d-=a[j][i] * x[i]
        y[j] = d / a[j][j]     # returning updated solution
    x=y
    return np.round(y,7)

print('\n\n')
print('jacobi iteration')

for i in range(0, 25):     # loop run for 25 iterations
    x = jacobi(a, x, b)
    print('\nIteration'+str(i+1),str(x),sep='\t')   
    
#swapping rows to make matrix diagonally dominate
#a[x],a[y]= a[y],a[x]    
if not isDDM(a,n): 
    a[0],a[2] = a[2],a[0]
    b[0],b[2] = b[2],b[0]


print(a , b, sep='\n\n')

if((isDDM(a, n))) :
    print ("True")
else :
    print ("False")
    
    
    
print('seidel iteration')
for i in range(0, 15):
    x = seidel(a, x, b)
    print('\niteration'+str(i+1),str(x),sep='\t')    

