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
# declare temperature range for function and fit
x = numpy.arange(243.15, 343.15, 10)
xp = numpy.arange(243.15, 343.15, 1)
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
        # linear regression
        z = numpy.polyfit(x, y, 1)
        p = numpy.poly1d(z)
        # plot measuring points with error bars
        ax.errorbar(x, y, (y * 0.0002), fmt='+', color="C" + str(color), capsize=5, markersize=5,
                    label=r"$f_{n=" + str(color + 1) + "}(T)$")
        ax.plot(xp, p(xp), color='grey', label=r"Linearer Fit")
        ax.legend(loc=1)
        ax.grid()
        color = color + 1
fig.savefig("plots/lintempdrift.png")
g.show()
