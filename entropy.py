from __future__ import division

from math import log, e
from numpy import arange
import matplotlib as mpl

mpl.use("pgf")
pgf_with_pdflatex = {
        "font.family": "serif",
    "font.size": 9,
    "text.usetex" : True,
    "pgf.rcfonts": False,
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": [
         r"\usepackage[utf8]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{kpfonts}",
         ]
}
mpl.rcParams.update(pgf_with_pdflatex)

import matplotlib.pyplot as plt

def H(a):
    """Binary Entropy"""
    return (a*log(1/a) + (1-a)*log(1/(1-a)))/log(2)




xdat = arange(0, 1, .001)
edat = [H(a) for a in xdat]
pdat = [a*log(1/a,2) + a*log(e,2) for a in xdat]
qdat = [1-(1-2*a)**2/(2*log(2,e)) for a in xdat]

plt.figure(figsize=[6.5,3.5])
plt.plot(xdat, pdat, label=r'$\alpha\log(1/\alpha)+\alpha\log e$', 
         color='#e41a1c')
plt.plot(xdat, qdat, label=r'$1-\frac{(1-2\alpha)^2}{2\ln 2}$',
         color='#377eb8')
plt.plot(xdat, edat, label=r'$H(\alpha)$',
         color='#4daf4a')
plt.xlabel(r'$\alpha$')
plt.legend(loc="upper left")

plt.savefig('entropy.pdf', format='pdf', bbox_inches='tight')
