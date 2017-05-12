from numpy import asarray


def plot_kinship(K):
    r"""Plot Kinship matrix.

    Parameters
    ----------
    K : array_like
        Kinship matrix.

    Examples
    --------

    .. plot::

        import limix
        import os
        limix.io.numpy.see_kinship(os.getcwd() + '/data/1000G_kinship.npy')
    """
    from matplotlib import pyplot as plt
    from matplotlib import cm as cm

    K = asarray(K, float)
    mi = K.min()
    ma = K.max()
    K = (K - mi) / (ma - mi)

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    cax = ax1.imshow(K, interpolation='nearest')
    fig.colorbar(cax)
    plt.show()
