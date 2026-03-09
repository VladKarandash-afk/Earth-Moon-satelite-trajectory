import numpy as np
import matplotlib.pyplot as plt

# Constants for the task (Earth-Moon)
T0 = 17.0652165601579625588917206249
miu = 0.012277471

# 1. Euler method
def Euler(f, a, b, x0, N):
    h = (b - a) / N
    T = [a]
    X = [x0]
    t = a
    x = x0
    for i in range(N):
        x = x + h * f(t, x)
        t = t + h
        T.append(t)
        X.append(x)
    return T, X

# 2. Runge-Kutta method of order 4
def RK4(f, a, b, x0, N):
    h = (b - a) / N
    T = [a]
    X = [x0]
    t = a
    x = x0
    for i in range(N):
        K1 = h * f(t, x)
        K2 = h * f(t + h/2, x + K1/2)
        K3 = h * f(t + h/2, x + K2/2)
        K4 = h * f(t + h, x + K3)
        x = x + (K1 + 2*K2 + 2*K3 + K4) / 6
        t = t + h
        T.append(t)
        X.append(x)
    return T, X

# 3.Dormand-Prince method
def DP(f, a, b, x0, N):
    h = (b - a) / N
    T = [a]
    X = [x0]
    t = a
    x = x0
    for i in range(N):
        D1 = h * f(t, x)
        D2 = h * f(t + h/5, x + D1/5)
        D3 = h * f(t + 3*h/10, x + 3*D1/40 + 9*D2/40)
        D4 = h * f(t + 4*h/5, x + 44*D1/45 - 56*D2/15 + 32*D3/9)
        D5 = h * f(t + 8*h/9, x + 19372*D1/6561 - 25360*D2/2187 + 64448*D3/6561 - 212*D4/729)
        D6 = h * f(t + h, x + 9017*D1/3168 - 355*D2/33 + 46732*D3/5247 + 49*D4/176 - 5103*D5/18656)
        # Calculation of a new point coordinates
        x = x + 35*D1/384 + 500*D3/1113 + 125*D4/192 - 2187*D5/6784 + 11*D6/84
        t = t + h
        T.append(t)
        X.append(x)
    return T, X

# System functions
def f1(t, x, y, v):
    return x + 2*v - (1-miu)*(x+miu)/((x+miu)**2 + y**2)**(1.5) - miu*(x-1+miu)/((x-1+miu)**2 + y**2)**(1.5)

def f2(t, x, y, u):
    return y - 2*u - (1-miu)*y/((x+miu)**2 + y**2)**(1.5) - miu*y/((x-1+miu)**2 + y**2)**(1.5)

def fVectorial(t, x):
    # Vector form: x'=u, u'=f1(x, y, v), y'=v, v'=f2(x, y, u)
    return np.array([x[1], f1(t, x[0], x[2], x[3]), x[3], f2(t, x[0], x[2], x[1])])

# Support functions for methods' launch
def solveBVP1(f, a, b, alpha, beta, N):
    T, X = Euler(f, 0, T0, np.array([a, alpha, b, beta]), N)
    X = np.array(X)
    return T, X[:, 0], X[:, 2]

def solveBVP2(f, a, b, alpha, beta, N):
    T, X = RK4(f, 0, T0, np.array([a, alpha, b, beta]), N)
    X = np.array(X)
    return T, X[:, 0], X[:, 2]

def solveBVP3(f, a, b, alpha, beta, N):
    T, X = DP(f, 0, T0, np.array([a, alpha, b, beta]), N)
    X = np.array(X)
    return T, X[:, 0], X[:, 2]

if __name__ == "__main__":
    print("Calculating... Please, wait.")
    
    # Starting conditions
    a_init = 0.994
    b_init = 0
    alpha_init = 0
    beta_init = -2.00158510637908252240537862224
    
    # Calculations using different methods
    T1, X1, Y1 = solveBVP1(fVectorial, a_init, b_init, alpha_init, beta_init, 24000) # Euler
    T2, X2, Y2 = solveBVP2(fVectorial, a_init, b_init, alpha_init, beta_init, 6000)  # RK4
    T3, X3, Y3 = solveBVP3(fVectorial, a_init, b_init, alpha_init, beta_init, 5000)  # DP
    
    # Visualisations build-up
    plt.figure(figsize=(8, 6))
    plt.plot(X1, Y1, label="Euler")
    plt.plot(X2, Y2, label="RK4")
    plt.plot(X3, Y3, label="Dormand-Prince")
    
    # Pinpoiting Earth and Moon positions
    plt.scatter([-miu, 1-miu], [0, 0], color="red", zorder=5, label="Earth and Moon")
    
    plt.title("Numerical methods comparison")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()
