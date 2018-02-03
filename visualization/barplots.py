
from . import utils
import numpy

def multiple_bar_plot(ax, data):
    labels, values = zip(*data)
    values = numpy.array(values)
    N = len(labels)

    utils.despine(ax)
    ind = numpy.arange(len(values[0]))+1
    total_width = 0.8
    width = total_width/N
    base = 0.5*width*(N-1)
    for i in range(N):
        ax.bar(ind-base+width*i, values[i], width=width, label=labels[i])
    ax.set_xticks(ind)
    ax.yaxis.set_major_formatter(utils.percentages)
    ax.legend()


def stacked_bar_plot(ax, data, divergent=False):
    labels, values = zip(*data)
    values = numpy.array(values)

    utils.despine(ax)
    colors = ['#fa7d26','#fdbb7e','#c8d0d9','#a4cce8','#62a3cc']
    ind = numpy.arange(len(labels))
    base = (-(values[:,0]+values[:,1]+values[:,2]/2.0) if divergent
            else numpy.zeros(len(labels)))
    for i in range(5):
        ax.barh(ind, values[:,i], align='center', height=0.75,
                color=colors[i], left=base+values[:,:i].sum(axis=1))
    ax.set_yticks(ind)
    ax.set_yticklabels(labels)
    ax.xaxis.set_major_formatter(utils.percentages)

