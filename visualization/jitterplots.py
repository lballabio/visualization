
import random
import numpy
from matplotlib import ticker

def _spaced(N, x, dx):
    n = N//2
    if N % 2 == 1:
        return ([x-dx*i for i in reversed(range(1,n+1))] +
                [x] +
                [x+dx*i for i in range(1,n+1)])
    else:
        return ([x-dx*(i+0.5) for i in reversed(range(n))] +
                [x+dx*(i+0.5) for i in range(n)])

def _rows(N, n_max):
    return N//n_max + (1 if N%n_max else 0)

def _ns(N, n_max):
    m = _rows(N, n_max)
    n = N // m
    r = N % m
    return [n+1]*r + [n]*(m-r)

def _shifts(N, n_max, dy):
    return _spaced(_rows(N, n_max), 0.0, dy)

def regular_xy(N, x, y, n_max=10, dx=0.1, dy=0.25):
    "Generates N regularly-spaced points around (x,y)"
    groups = zip(_ns(N, n_max),
                 _shifts(N, n_max, dy))
    ps = []
    for n,dy in groups:
        ps += [ (z,y+dy) for z in _spaced(n,x,dx) ]
    return ps

def jittered_xy(N, x, y, width_x=0.9, width_y=0.9):
    "Generates N jittered points around (x,y)"
    x_min, x_max = x-width_x/2, x+width_x/2
    y_min, y_max = y-width_y/2, y+width_y/2
    return [ (random.uniform(x_min, x_max), random.uniform(y_min, y_max))
             for i in range(N) ]


def jitter_plot(ax, data, jitter=True, highlights=None,
                markersize=None, **kwargs):
    label_tag, value_tag, count_tag = data.columns
    labels = sorted(set(data[label_tag]))
    idx = numpy.arange(len(labels))
    ax.set_xlim(idx[0]-0.5, idx[-1]+0.5)
    ax.set_xticks(idx)
    ax.set_xticklabels(labels, fontsize=14)
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.xaxis.grid(True, 'minor', color='#999999')

    max_n = data[value_tag].max()
    idy = numpy.arange(max_n+1)
    ax.set_ylim(idy[0]-0.5, idy[-1]+0.5)
    ax.set_yticks(idy)
    ax.set_yticklabels(idy, fontsize=14)

    f = jittered_xy if jitter else regular_xy
    for l in labels:
        points = []
        column = data[data[label_tag] == l]
        x = labels.index(l)
        for y,c in zip(column[value_tag],column[count_tag]):
            points += f(c, x, y, **kwargs)
        xs, ys = zip(*sorted(points, key=lambda x: (x[1],x[0])))
        ax.plot(xs, ys, 'o', color='white',
                markersize=markersize, markeredgecolor='0.3')
        if highlights:
            for g,color in highlights:
                n = g(len(xs))
                ax.plot(xs[n:n+1], ys[n:n+1], 'o', color=color)