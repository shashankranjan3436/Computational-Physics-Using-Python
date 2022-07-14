# Introduction
Computational physics is the study of scientific problems using computational methods; it combines computer science, physics and applied mathematics to develop scientific solutions to complex problems. Computational physics complements the areas of theory and experimentation in traditional scientific investigation.

# Methods
## Gauss Elimination
the Gaussian elimination method is known as the row reduction algorithm for solving linear equations systems. It consists of a sequence of operations performed on the corresponding matrix of coefficients. We can also use this method to estimate either of the following:
- The rank of the given matrix
- The determinant of a square matrix
- The inverse of an invertible matrix

## Gauss Elimination with Partial Pivoting

## Gauss Jordan Elimination
The Gauss-Jordan method is similar to the Gaussian elimination process, except that the entries both above and below each pivot are zeroed out. After performing Gaussian elimination on a matrix, the result is in row echelon form, while the result after the Gauss-Jordan method is in reduced row echelon form.

## Gauss-Siedel Iteration & Jacobi Iteration
- Gauss-Seidel Method
The Gauss-Seidel method is the most commonly used iterative method. Assume that we are given a set of n 
equations: [A]{X} = {B}
If the diagonal elements are all nonzero, the first equation can be solved for x 1, the second for x2, the third for x3 and 
so on. As each new x value is computed for the Gauss-Seidel method, it is immediately used in the next equation to 
determine another x value. Thus, if the solution is converging, the best available estimates will be employed.
The Gauss-Seidel method can also exhibit some shortcomings. For this method to converge to the real value, the 
diagonal element must be greater than the off-diagonal element for each row i.e., the matrix must be Diagonally 
dominant.
- Jacobi Iteration
This is an alternative approach which utilizes a somewhat different tactic. Rather than using the latest available x’s, 
this technique computes a set of new x’s on the basis of a set of old x’s. Thus, as new values are generated, they are 
not immediately used but rather are retained for the next iteration. 
Although there are certain cases where the Jacobi method is useful, Gauss-Seidel’s utilization of the best available 
estimates usually makes it the method of preference.

## Power Method
The Power Method is used to find a dominant eigenvalue (one having the largest absolute value), if one exists, and a corresponding eigenvector. To apply the Power Method to a square matrix A, begin with an initial guess u0 for the eigenvector of the dominant eigenvalue.

## Euler and Ranga Kutta 4 Method
Runge–Kutta method is an effective and widely used method for solving the initial-value 
problems of differential equations. Runge–Kutta method can be used to construct high 
order accurate numerical method by functions' self without needing the high order 
derivatives of functions. Generalized form of this method can be written as
where, is called an increment function, which can be interpreted as a 
representative slope over the interval.
Various types of Runge-Kutta methods can be devised by employing different numbers of terms 
in the increment function as specified by n. The first-order RK method with n=1 is Euler’s 
method.
- Fourth order Runge-Kutta Method (RK4 Method)
The most popular RK methods are fourth order. The most commonly used form is 
yi+1 = yi + 1/6(k1 + 2k2 + 2k3+ k4) *h
where,k1 = f(xi ,yi)
h = step size
k2 = f(xi+h/2 ,yi+k1h/2) 
k3 = f(xi+h/2 ,yi+k2h/2)
k4 = f(xi+h ,yi+k3h)
Each of the k’s represents a slope. The equation then represents a weighted average
of these to arrive at the improved slope.

## Finite Difference & Shooting Method
- Shooting Method
The shooting method is based on converting the boundary-value problem into an equivalent initial-value problem. A 
trial-and-error approach is then implemented to solve the initial-value version. To solve these equations, we require an 
initial value. We, then, guess a value. The solution is then obtained by integrating the equations simultaneously.
For nonlinear boundary-value problems, linear interpolation or extrapolation through two solution points will not 
necessarily result in an accurate estimate of the required boundary condition to attain an exact solution. An alternative 
is to perform three applications of the shooting method and use a quadratic interpolating polynomial to estimate the 
proper boundary condition. However, it is unlikely that such an approach would yield the exact answer, and additional 
iterations would be necessary to obtain the solution.
- Finite Difference Method
In this technique, finite divided differences are substituted for the derivative s in the original equation. Thus, a linear 
differential equation is transformed into a set of simultaneous algebraic equations that can be solved using different 
methods learnt earlier
## 
