import numpy as np
import matplotlib.pyplot as plt

# Here plotting should occur


# TODO Make it plot data from mongoDB
def plot_demo(_p, name=''):
    plt.plot(_p.best, label="Best")
    plt.plot(_p.mean, label="Mean")
    plt.yticks(np.linspace(min(min(_p.best), min(_p.mean)),
                           max(max(_p.best), max(_p.mean)), num=10))
    plt.legend(loc='lower right')
    plt.savefig("".join([name, "rys.pdf"]), dpi=72)
    plt.clf()
