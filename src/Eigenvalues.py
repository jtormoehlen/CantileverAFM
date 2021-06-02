import scipy
from scipy.misc import derivative


# characteritic function
def f(x):
    return (scipy.cos(x) * scipy.cosh(x)) + 1


# first derivation of char. function f
# f' = (scipy.cos(x) * scipy.sinh(x)) - (scipy.sin(x) * scipy.cosh(x))
def g(x):
    return derivative(f, x, dx=1.0E-6, n=1)


# my = 0.1
def h(x):
    return (scipy.cos(x)*scipy.cosh(x))+1+(0.1*x*((scipy.cos(x)*scipy.cosh(x))-(scipy.sin(x)*scipy.sinh(x))))


def k(x):
    return derivative(h, x, dx=1.0E-6, n=1)


# computation of eigenvalues alpha_n and epsilon_n via newton procedure
for i in range(0, 4):
    alpha = (i + (1 / 2)) * scipy.pi
    epsilon = alpha
    for j in range(1, 10):
        alpha = alpha - (f(alpha) / g(alpha))
        epsilon = epsilon - (h(epsilon) / k(epsilon))
    print("alpha_" + str(i+1) + "=" + str(alpha) + "\n" + "epsilon_" + str(i+1) + "=" + str(epsilon))

# output yields for alpha_n:
# 1.8751040687119611
# 4.694091132974175
# 7.854757438237613
# 10.995540734875467

# and epsilon_n:
# 1.7283615639650685
# 4.399630969774218
# 7.451057011310791
# 10.521784756827731
