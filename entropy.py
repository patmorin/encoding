from __future__ import division

from math import log, e

def H(a):
    """Binary Entropy"""
    return (a*log(1/a) + (1-a)*log(1/(1-a)))/log(2)


if __name__ == "__main__":
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
    
    xdat = arange(0, 1, .001)
    edat = [H(a) for a in xdat]
    pdat = [a*log(1/a,2) + a*log(e,2) for a in xdat]
    qdat = [1-(1-2*a)**2/(2*log(2,e)) for a in xdat]
    
    plt.figure(figsize=[6.5,3])
    plt.xlim(0,1)
    plt.xticks([x/4 for x in range(5)], ['0', '$1/4$', '$1/2$', '$3/4$', '1'])
    plt.plot(xdat, pdat, label=r'$\alpha\log(1/\alpha)+\alpha\log e$', 
             color='#d95f02', linestyle='--')
    plt.plot(xdat, qdat, label=r'$1-\frac{(1-2\alpha)^2}{2\ln 2}$',
             color='#1b9e77', linestyle=':')
    plt.plot(xdat, edat, label=r'$H(\alpha)$',
             color='#7570b3', linestyle='-')
    plt.xlabel(r'$\alpha$')
    plt.legend(loc="upper left", framealpha=0.8)
    
    plt.savefig('entropy.pdf', format='pdf', bbox_inches='tight')
