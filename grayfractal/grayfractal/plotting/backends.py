""" Plotting backends using different libraries. """

from itertools import chain


class MatplotlibBackend(object):
    """ Backend wrapping Matplotlib functionality. """
    def __init__(self):
        try:
            from matplotlib import pyplot as plt
        except ModuleNotFoundError as err:
            print('Backend library not installed. Try another.')
            raise err

        try:
            import seaborn
        except ImportError:
            pass

        self.plt = plt

    @property
    def name(self):
        return 'matplotlib'

    def plot_fractal(self, fractal, axes=None, out='display', **kwargs):
        axes = self._maybe_make_new_axes(axes)
        for generation in fractal.generations:
            axes = self.plot_generation(generation, axes=axes, out=None)
        if out == 'display': self.plt.show()
        return axes

    def plot_generation(self, generation, axes=None, out='display', **kwargs):
        axes = self._maybe_make_new_axes(axes)
        points = generation.points
        x = [p[0]/2**generation.order for p in points]
        y = [p[1]/2**generation.order for p in points]
        axes.step(x,y, where='post')
        if out == 'display': self.plt.show()
        return axes

    def _maybe_make_new_axes(self, axes):
        if axes == None:
            axes = self.plt.axes()
            axes.set_aspect('equal')
        return axes


class PlotlyBackend(object):
    """ Backend wrapping Plotly functionality"""
    def __init__(self):
        try:
            from plotly import graph_objects as go
        except ModuleNotFoundError as err:
            print('Backend not installed. Try another.')
            raise err

        self.go = go

    @property
    def name(self):
        return 'plotly'

    def plot_fractal(self, fractal):
        for generation in fractal.generations:
            self.plot_generation(generation)

    def plot_generation(self, generation):
        raise NotImplementedError
