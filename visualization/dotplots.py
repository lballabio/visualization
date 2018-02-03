
def dot_plot(ax, data):
    N = len(data)
    ind = range(1,N+1)
    x1 = data[data.columns[0]]
    x2 = data[data.columns[1]]

    ax.set_ylim(0,N+1)
    ax.yaxis.set_ticks(ind)
    ax.yaxis.set_ticklabels(data.index)
    for i,item in enumerate(data.index):
        ax.hlines(i+1, x1[i], x2[i], linestyle='solid',color='#888888')
    ax.plot(x1, ind, 'o', color='#eb7d3c', markersize=8, label=data.columns[0])
    ax.plot(x2, ind, 'o', color='#1e3256', markersize=8, label=data.columns[1])
    ax.legend(loc='best', numpoints=1)


def slopegraph(ax, data):
    N = len(data)
    x1 = data[data.columns[0]]
    x2 = data[data.columns[1]]
    ind = [1,2]

    ax.xaxis.set_ticks(ind)
    ax.xaxis.set_ticklabels(data.columns)

    for i in range(N):
        p, = ax.plot(ind, [x1[i],x2[i]], 'o', markersize=8,
                     label=data.index[i])
        ax.plot(ind, [x1[i],x2[i]], '-', color=p.get_color())
    ax.legend(loc='best', numpoints=1)

