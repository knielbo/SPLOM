import sys
import numpy as np
import pandas as pd

import scipy.stats as sps
import matplotlib as mpl

from matplotlib import colors as mcolors
from matplotlib import pyplot as plt
"""
Scatter PLOt Matrix
"""

def getidxs(l,val):
    return [i for i, x in enumerate(l) if x == val]

def splom(M,featurenames,classvar=False,order=1,fname="splom.png"):
    mpl.rcParams.update({'text.usetex': False,
                        'font.family': 'serif',
                        'font.serif': 'cmr10',
                        'font.weight':'bold',
                        'mathtext.fontset': 'cm',
                        'axes.unicode_minus'  : False
                        })
    n = M.shape[1]
    if classvar:
        c_set = list(set(classvar))
        colors = ["r","g","b"]

    fig, ax = plt.subplots(n,n)
    fig.set_size_inches(16,16)
    fig.subplots_adjust(wspace = .35, hspace = .25)
    if classvar:
        c_set = list(set(classvar))
        colors = sorted([color for color in list(mcolors.BASE_COLORS.keys()) if color != "w"][:len(c_set)], reverse = True)
    for i, x in enumerate(M.T):
        for ii, y in enumerate(M.T):
            if i == ii:
                if classvar:
                    for j, clss in enumerate(c_set):
                        c_x = x[getidxs(classvar,clss)]
                        mu = np.mean(c_x)
                        sigma =  np.std(c_x)
                        binsize = 20
                        m, bins, patches = ax[i,ii].hist(c_x, binsize, facecolor= colors[j], density=1, alpha=0.75)
                        z = sps.norm.pdf(bins, mu, sigma)
                        ax[i,ii].plot(bins, z, linewidth=2, color=colors[j],label=c_set[j])
                        ax[i,ii].set_xlabel(featurenames[i])
                    ax[i,ii].legend(loc="best",edgecolor=None,shadow=False)
                else:
                    mu = np.mean(x)
                    sigma =  np.std(x)
                    binsize = 20# optimal binning
                    m, bins, patches = ax[i,ii].hist(x, binsize, color="k",density=1, alpha=0.75)
                    z = sps.norm.pdf(bins, mu, sigma)
                    ax[i,ii].plot(bins, z, 'r--', linewidth=2)
                    ax[i,ii].set_xlabel(featurenames[i])
            else:
                if classvar:
                    for j, clss in enumerate(c_set):
                        c_x = x[getidxs(classvar,clss)]
                        c_y = y[getidxs(classvar,clss)]
                        p = np.poly1d(np.polyfit(c_x, c_y, order))
                        xp = np.linspace(min(c_x), max(c_x), len(x))
                        ax[i,ii].plot(c_x, c_y,'{}.'.format(colors[j]), xp, p(xp), '{}-'.format(colors[j]), linewidth = 2)
                        ax[i,ii].set_xlabel(featurenames[i])
                        ax[i,ii].set_ylabel(featurenames[ii])
                else:
                    p = np.poly1d(np.polyfit(x, y, order))
                    xp = np.linspace(min(x), max(x), len(x))
                    ax[i,ii].plot(x, y, 'k.', xp, p(xp), 'r-', linewidth = 2)
                    ax[i,ii].set_xlabel(featurenames[i])
                    ax[i,ii].set_ylabel(featurenames[ii])
    plt.savefig(fname)
    plt.close()
    print("Splom written to file: {}".format(fname))
    return fig

def main():
    fname = sys.argv[1]
    df = pd.read_csv(fname, header = 0)
    featurenames = [name[0].upper()+name[1:] for name in list(df.columns)]
    if df.columns[-1] == "class":
        c = df["class"].tolist()
        M = np.array(df.iloc[:,0:-1])
        splom(M,featurenames,classvar=c,order=1,fname="splom.png")
    else:
        M = np.array(df)
        splom(M,featurenames,classvar=False,order=1,fname="splom.png")

if __name__ == '__main__':
    main()
