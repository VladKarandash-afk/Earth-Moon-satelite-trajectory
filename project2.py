import numpy as np

# Dormand-Prince method
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
        
        x = x + 35*D1/384 + 500*D3/1113 + 125*D4/192 - 2187*D5/6784 + 11*D6/84
        t = t + h
        T.append(t)
        X.append(x)
    return T, X

# Test functions
def f1(t, x): 
    return x

def f2(t, x): 
    return x**2 + 1

def f3(t, x): 
    return -x

def f4(t, x): 
    return 2 * x * t

# Check of the accuracy of the method on different equations
def Test1(N):
    Err = []
    
    # Values for x'=x, x(0)=1 on [0, 5]
    T1, X1 = DP(f1, 0, 5, 1, N) 
    Err.append(abs(X1[-1] - np.exp(5)))
    
    # Values for x'=x^2+1, x(-pi/4)=0 on [-pi/4, 0]
    T2, X2 = DP(f2, -np.pi/4, 0, 0, N) 
    Err.append(abs(X2[-1] - 1))
    
    # Values for x'=-x, x(0)=1 on [0, 5]
    T3, X3 = DP(f3, 0, 5, 1, N) 
    Err.append(abs(X3[-1] - np.exp(-5)))
    
    # Values for x'=2*x*t, x(0)=1 on [0, 5]
    T4, X4 = DP(f4, 0, 5, 1, N) 
    Err.append(abs(X4[-1] - np.exp(25)))
    
    return Err

if __name__ == "__main__":
    N = 6000
    errors = Test1(N)
    
    print(f"Errors for different funtions (iterations: {N}):")
    print(f"f1: {errors[0]:.4e}")
    print(f"f2: {errors[1]:.4e}")
    print(f"f3: {errors[2]:.4e}")
    print(f"f4: {errors[3]:.4e}")
