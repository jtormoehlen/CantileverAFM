import matplotlib.pyplot as g
import numpy
import scipy


# define phaseshift function
def phase(x, f_0, q):
    y = (numpy.arctan((-x / f_0) / (q * (1.0 - ((x * x) / (f_0 * f_0))))) * (
            180.0 / scipy.pi)) - numpy.where(x >= 75.0, 180.0, 0.0)
    return y


# declare parameters
f_0 = 75.0
# declare frequency range
x = numpy.arange(74.9, 75.1, 0.0001)
# plot functions
g.plot(x / f_0, phase(x, f_0, 1000.0), label=r"$Q=1000$")
g.plot(x / f_0, phase(x, f_0, 5000.0), label=r"$Q=5000$")
g.plot(x / f_0, phase(x, f_0, 10000.0), label=r"$Q=10000$")
g.xlabel(r"$f / f_0$", fontsize=16)
g.ylabel(r"Phasenverschiebung $\varphi$ in [Grad]", fontsize=16)
g.xticks([1.0])
g.legend()
g.grid()
g.savefig("plots/phasenverschiebung.png")
g.show()
