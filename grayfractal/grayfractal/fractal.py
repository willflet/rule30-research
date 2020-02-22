""" Base objects for working with fractal curves over integers. """

from copy import deepcopy
from itertools import chain
from .plotting import FractalPlotter


class Fractal(object):
    """ A collection of fractal generations, with global properties. """

    def __init__(self, growth_rule):
        """ Make a base case fractal. """

        self.rule = growth_rule

        base_generation = self.rule.base_generation
        base_generation._fractal = self
        self._generations = [base_generation]

        self._plotter = None

    @property
    def generations(self):
        return self._generations

    @property
    def order(self):
        return len(self.generations) -1

    def grow(self):
        new_generation = self.generations[-1].grow(in_place=False)
        self._generations.append(new_generation)

    @property
    def plotter(self):
        return self._plotter

    def plot(self, backend='matplotlib', **kwargs):
        self._maybe_make_new_plotter(backend)
        self.plotter.plot_fractal(self, **kwargs)

    def plot_generation(self, order, backend='matplotlib', **kwargs):
        if order > self.order:
            raise ValueError("Fractal hasn't grown this far!")
        self.generations[order].plot(backend=backend, **kwargs)

    def _maybe_make_new_plotter(self, backend):
        if self.plotter is None:
            self._plotter = FractalPlotter(backend=backend)
        elif backend.lower() != self.plotter.backend.name:
            self._plotter = FractalPlotter(backend=backend)


class Generation(object):
    """ A single generation of the fractal. """

    def __init__(self, rule, order=0, points=[[0,0]], fractal=None):
        """ Create a new generation of the fractal. """
        self._rule = rule
        self._order = order
        self._points = points
        self._fractal = fractal

    @property
    def rule(self):
        return self._rule

    @property
    def fractal(self):
        return self._fractal

    @property
    def order(self):
        return self._order

    @property
    def points(self):
        return self._points + [self._end_point]

    @property
    def _end_point(self):
        return [2**self.order, 0]

    def grow(self, in_place=False):
        return self.rule.apply(self, in_place=in_place)

    def plot(self, backend='matplotlib', **kwargs):
        self.fractal._maybe_make_new_plotter(backend)
        self.fractal.plotter.plot_generation(self, **kwargs)
