import math

import numpy as np
import matplotlib.pyplot as plt


def add_stats(ax, data):
    """
    Add a text box with stats about the data
    :param ax: Axis
    :param data: Data
    """
    ax.text(
        0.7, 0.7,
        '$\mu$: {:.3e}\n$\sigma$: {:.3e}\n$\%_{{50}}$: {:.3e}'.format(
            np.average(data),
            np.std(data),
            np.median(data),
        ),
        transform=ax.transAxes
    )


def scatter_delta(data, fmt='.', ylabel=None, xlabel=None, ydeltalabel=None, figsize=None, c=None):
    """
    Plot a scatter flor with the delta bellow
    :param data:
        A list of tuples such as (x, y, [yerr], [flags], [title])
    :param fmt:
        Format of the dots
    :param ylabel:
        Y Axis label
    :param xlabel:
        X Axis label
    :param ydeltalabel:
        (Y-X) Axis label (bottom plot)
    :param figsize:
        Figure size
    :param c:
        A colour, or list of colours
    """
    assert type(data) == list

    nplots = len(data)
    nrows = math.ceil(nplots / 2)

    if c is None:
        c = plt.get_cmap('Paired')(range(nplots))
    elif not isinstance(c, list):
        c = [c] * nrows

    plt.figure(figsize=figsize)

    for i in range(nplots):
        assert type(data[i] == tuple)

        if len(data[i]) == 2:
            x, y = data[i]
            yerr = None
            flag = None
            title = None
        elif len(data[i]) == 3:
            x, y, third = data[i]
            flag = None
            if isinstance(third, str):
                title, yerr = third, None
            else:
                title, yerr = None, third
        elif len(data[i]) == 4:
            x, y, yerr, fourth = data[i]
            if isinstance(fourth, str):
                title, flag = fourth, None
            else:
                title, flag = None, fourth
        elif len(data[i]) == 5:
            x, y, yerr, flag, title = data[i]
        else:
            raise Exception('Unexpected number of elements in tuple!')

        col = i % 2
        row = ((i - col) // 2)

        gs = plt.GridSpec(3, 1)

        top = 0.95 - (0.9 / nrows) * row - 0.05
        bottom = 0.95 - (0.9 / nrows) * (row + 1) + 0.05

        if col == 0:
            left = 0.05
            right = 0.47
        else:
            left = 0.53
            right = 0.95

        gs.update(left=left, right=right, bottom=bottom, top=top, hspace=0)

        # Scatter
        ax1 = plt.subplot(gs[:-1, :])
        ax1.errorbar(x, y, yerr=yerr, fmt=fmt, c=c[i])
        ax1.set_xticks([])
        ax1.grid(True, linestyle=':')
        if flag is not None:
            ax1.scatter(x[flag], y[flag], marker='o', c='red', alpha=0.5)
        if ylabel:
            ax1.set_ylabel(ylabel)
        if title:
            ax1.set_title(title)

        # Delta
        ax2 = plt.subplot(gs[-1, :])
        ax2.errorbar(x, y - x, yerr=yerr, fmt=fmt, c=c[i])
        ax2.grid(True, linestyle=':')
        if flag is not None:
            ax2.scatter(x[flag], (y - x)[flag], marker='o', c='red', alpha=0.5)
        if ydeltalabel:
            ax2.set_ylabel(ydeltalabel)
        if xlabel:
            ax2.set_xlabel(xlabel)


def add_stats(ax, data):
    """
    Add a box with statistics about the data
    """
    ax.text(
        0.7, 0.7,
        '$\mu$: {:.3e}\n$\sigma$: {:.3e}\n$\%_{{50}}$: {:.3e}'.format(
            np.average(data),
            np.std(data),
            np.median(data),
        ),
        transform=ax.transAxes
    )
