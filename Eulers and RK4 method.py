import numpy as np
import matplotlib.pyplot as plt


# function value (here 2nd derivative of x wrt t)
def func(x, t, v):
    return -x * c  # c=k/m


# exact solution value calculator
def ogFun(t, step, range_):
    Xorg = []
    for i in range(int(range_ / step) + 1):
        Xorg.append(x0 * np.cos(t[i]))
    Xorg = np.array(Xorg)
    return Xorg


# print the solutions
def prt(T1, X1, range_):
    print("\nt value      x value")
    for i in range(int(range_ / step) + 1):
        print("%0.2f" % T1[i], end="\t\t ")
        print(X1[i])


def Euler(x, t, v, step, range_):
    X1 = []
    T1 = []
    X1.append(x)
    T1.append(t)
    for i in range(int(range_ / step)):
        x_init = x
        x = x_init + step * v  # new x
        v = v + step * func(x_init, t, v)  # new v
        t += step  # new t
        X1.append(x)  # appending new values to list
        T1.append(t)
    X1 = np.array(X1)
    T1 = np.array(T1)
    plt.plot(T1,X1)

def RK4(x, t, v, step, range_):
    X1 = [x]
    T1 = [t]
    v = [v]
    for i in range(int(range_ / step)):
        k1 = v[i]
        k2 = v[i] - (X1[i]+(k1*step*0.5))*0.5*step
        k3 = v[i] - (X1[i] + (k2*step*0.5))*0.5*step
        k4 = v[i] - (X1[i] + k3*step)*step
        x_inti = X1[i] + ((k1+2*k2+2*k3+k4)/6)*step
        X1.append(x_inti)
        T1.append(T1[i]+step)
        v_inti = v[i] - X1[i]*step
        v.append(v_inti)
        plt.plot(T1,X1)

if __name__ == '__main__':
    x0 = 1
    t0 = 0
    v0 = 0
    c = 1
    step = 0.25
    range_ = 20
    Euler(x0, t0, v0, step, range_)
    RK4(x0, t0, v0, step, range_)
    plt.title("Assignment 8")
    plt.xlabel("t")
    plt.ylabel("x")
    plt.legend(['Euler','RK4'])
    # plt.savefig('graph2.png', dpi=300)
    plt.show()