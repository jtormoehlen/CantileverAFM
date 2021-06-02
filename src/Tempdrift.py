import matplotlib.pyplot as g
import numpy
import scipy


def f(x, epsilon):
    i = (1 / 12) * w * t * t * t
    m = rho * w * t * l
    c = ((epsilon * epsilon) / (2 * scipy.pi)) * scipy.sqrt(i / (l * l * l * m))
    return (c * scipy.sqrt((e_0 - (b * x * scipy.exp(-t_s / x))) * (1 + (a_l * (x - t_0))))) / 1000


# declare parameters
rho = 2336
w = 28E-6
t = 3E-6
l = 225E-6
e_0 = 167.5E+9
b = 15.8E+6
t_s = 317
a_l = 2.6E-6
t_0 = 293.15
# declare temperature range
x = numpy.arange(1, 1683, 1)
# subplot for every eigenvalue
fig, axs = g.subplots(nrows=2, ncols=2, sharex=True, sharey=False)
color = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax = axs[i, j]
        if j == 0:
            if i == 0:
                e_n = 1.7284
                ax.set_ylabel(r"Eigenfrequenz $f_n$ in [kHz]")
            else:
                e_n = 7.4511
                ax.set_xlabel(r"Temperatur $T$ in [K]")
                ax.set_ylabel(r"Eigenfrequenz $f_n$ in [kHz]")
        else:
            if i == 0:
                e_n = 4.3996
            else:
                e_n = 10.5218
                ax.set_xlabel(r"Temperatur $T$ in [K]")
        y = f(x, e_n)
        ax.plot(x, f(x, e_n), color="C" + str(color), label=r"$f(T,\epsilon_" + str(color + 1) + ")$")
        ax.plot(239.15, f(239.15, e_n), marker='+', markersize=20, color="C7", label=r"$T_0=293.15$K")
        ax.legend(loc=3)
        ax.grid()
        color = color + 1
fig.savefig("plots/tempdrift.png")
g.show()
