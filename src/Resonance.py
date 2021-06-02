import matplotlib.pyplot as g
import numpy
import scipy


# define resonance function
def resonance(x, a, f_0, q):
    y = (a / scipy.sqrt(((1 - ((x * x) / (f_0 * f_0))) * (1 - ((x * x) / (f_0 * f_0))))
                        + ((x * x) / (f_0 * f_0 * q * q)))) / 10000
    return y


# declare parameters
a = 1
f_0 = 75
# declare frequency range
x = numpy.arange(74.95, 75.05, 0.0001)
# plot functions
g.plot(x, resonance(x, a, f_0, 1000), label=r"$Q=1000$")
g.plot(x, resonance(x, a, f_0, 5000), label=r"$Q=5000$")
g.plot(x, resonance(x, a, f_0, 10000), label=r"$Q=10000$")
g.xlabel(r"Frequenz $f$ in [kHz]", fontsize=16)
g.ylabel(r"Amplitude $A$ (a.u.)", fontsize=16)
g.xticks([75.0])
g.legend()
g.grid()
g.savefig("plots/resonanzkurve.png")
g.show()
