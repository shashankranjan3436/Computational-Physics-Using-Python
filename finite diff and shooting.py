import numpy as np
import matplotlib.pyplot as plt

F1 = lambda z: z

F2 = lambda T: hPrime * (T - Ta)


def pprint(xAr, arr1, arr2):
    template = "{0:<19} {1:<25} {2:<25}"
    print(template.format("x value", "T (Shooting method)",
                          "T (Finite Difference method)"))
    for i in range(n+1):
        print(template.format(xAr[i], arr1[i], arr2[i]))


def RK4(x, T, z):
    T_list = [T]
    x_list = [x]
    for i in range(n):
        k1 = F1(z)
        l1 = F2(T)

        k2 = F1(z + (h * l1 / 2.0))
        l2 = F2(T + (h * k1 / 2.0))

        k3 = F1(z + (h * l2 / 2.0))
        l3 = F2(T + (h * k2 / 2.0))

        k4 = F1(z + h * l3)
        l4 = F2(T + h * k3)

        T += (k1 + 2.0 * k2 + 2.0 * k3 + k4) * h / 6.0
        z += (l1 + 2.0 * l2 + 2.0 * l3 + l4) * h / 6.0
        x += h

        T_list.append(T)
        x_list.append(x)

    return T, np.array(T_list), np.array(x_list)


def shooting(z1, z2):
    T10_1, TArr1, xArr1 = RK4(x0, T0, z1)
    T10_2, TArr2, xArr2 = RK4(x0, T0, z2)

    z0 = z1 + (z2 - z1) * (T10 - T10_1) / (T10_2 - T10_1)

    return RK4(x0, T0, z0)


def gauss(A, b):
    m = n - 1
    Sol = np.zeros(m)
    # elimination
    for k in range(m - 1):
        for i in range(k + 1, m):
            if A[i][k] == 0:
                continue
            fact = A[k, k] / A[i, k]
            for j in range(k, m):
                A[i, j] = A[k, j] - A[i, j] * fact
            b[i] = b[k] - b[i] * fact

    # back-sub
    Sol[m - 1] = b[m - 1] / A[m - 1, m - 1]
    for i in range(n - 2, -1, -1):
        sum_ = b[i]
        for j in range(i + 1, m):
            sum_ -= A[i][j] * Sol[j]
        Sol[i] = sum_ / A[i][i]

    return Sol


def finiteDiff():
    # generating vector b
    b = np.zeros(n - 1)
    for i in range(n - 1):
        if i == 0:
            b[i] = hPrime * (h ** 2) * Ta + T0
        elif i == n - 2:
            b[i] = hPrime * (h ** 2) * Ta + T10
        else:
            b[i] = hPrime * (h ** 2) * Ta

    # generating matrix A
    A = np.zeros((n - 1, n - 1))
    for i in range(n - 1):
        for j in range(n - 1):
            if i == j:
                A[i, j] = 2 + hPrime * (h ** 2)
            elif i == j + 1 or i == j - 1:
                A[i, j] = -1
            else:
                A[i, j] = 0

    Sol = gauss(A, b)
    Sol = np.insert(Sol, 0, T0)
    Sol = np.append(Sol, T10)

    return Sol


if __name__ == '__main__':
    # given values
    hPrime = 0.01
    Ta = 20
    T0, T10 = 40, 200
    rodLen = 10
    x0 = 0
    #
    n = 16
    h = (rodLen - x0) / n
    # assumed values
    z1, z2 = 10, 20
    #
    _, TArr, xArr = shooting(z1, z2)
    TArrF = finiteDiff()
    pprint(xArr, TArr, TArrF)
    #
    plt.plot(xArr, TArr, color="#00CC00", linewidth="3")
    plt.plot(xArr, TArrF, color='b', linestyle='--', dashes=(5, 5))
    plt.title("Boundary value problem graph")
    plt.xlabel("x")
    plt.ylabel("T")
    plt.legend(["Shooting method", "Finite-Difference method"])
    # plt.savefig("graph.png", dpi=600)
    plt.show()

