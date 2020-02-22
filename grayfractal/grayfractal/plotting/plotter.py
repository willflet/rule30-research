""" Graphical plotting of fractals. """

from .backends import MatplotlibBackend, PlotlyBackend


BACKENDS = dict(
    matplotlib=MatplotlibBackend,
    plotly=PlotlyBackend
)


class FractalPlotter(object):
    """ Plotting API for Fractal objects. """

    def __init__(self, backend='matplotlib'):
        """ Make a new plotter. """
        try:
            self.backend = BACKENDS[backend.lower()]()
        except KeyError:
            raise ValueError(
                "Unrecognized backend. Must be one of {}".format(BACKENDS.keys())
            )

    def plot_fractal(self, fractal, *args, **kwargs):
        self.backend.plot_fractal(fractal, *args, **kwargs)

    def plot_generation(self, generation, *args, **kwargs):
        self.backend.plot_generation(generation, *args, **kwargs)
