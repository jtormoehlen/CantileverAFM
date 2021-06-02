import matplotlib.pyplot as g
import numpy
import scipy


# define eigenoscillation function
def modes(x, alpha):
    y = (scipy.cos(alpha * x) - scipy.cosh(alpha * x) - (
            ((scipy.cos(alpha) + scipy.cosh(alpha)) / (scipy.sin(alpha) + scipy.sinh(alpha))) * (
            scipy.sin(alpha * x) - scipy.sinh(alpha * x)))) / 2
    return y


# subplot for every eigenvalue
x = numpy.arange(0, 1, 0.001)
fig, axs = g.subplots(nrows=2, ncols=2, sharex=True, sharey=True)
color = 0
for i in range(0, 2):
    for j in range(0, 2):
        ax = axs[i, j]
        if j == 0:
            if i == 0:
                a_n = 1.8751
                ax.set_ylabel(r"Auslenkung $W(x,\alpha)$ (a.u.)")
            else:
                a_n = 7.8548
                ax.set_xlabel(r"Position $x$")
                ax.set_ylabel(r"Auslenkung $W(x,\alpha)$ (a.u.)")
        else:
            if i == 0:
                a_n = 4.6941
            else:
                a_n = 10.9955
                ax.set_xlabel(r"Position $x$")

        ax.plot(x, modes(x, a_n), color="C" + str(color),
                label=r"$W(x,\alpha_" + str(color + 1) + ")$")
        ax.plot(x, -modes(x, a_n), color="C" + str(color), linestyle='--')
        g.xticks([0.0, 0.5, 1.0])
        ax.legend(loc=2)
        ax.grid()
        color = color + 1
fig.savefig("plots/eigenschwingungen.png")
g.show()
