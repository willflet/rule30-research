""" Mathematical objects describing growth of a cyclic binary fractal. """

from copy import deepcopy
from itertools import chain
from .plotting import FractalPlotter

class Fractal(object):
    """ A collection of fractal generations, with global properties. """

    def __init__(self):
        """ Make a base case fractal. """
        self._generations = [Generation(self)]
        self._plotter = None

    @property
    def order(self):
        return len(self._generations) - 1

    @property
    def generations(self):
        return self._generations

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

    def __init__(self, fractal):
        """ Create a new generation of the fractal. """
        self._fractal = fractal
        self._order = 0
        self._points = [[0,0]]

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

    def plot(self, backend='matplotlib', **kwargs):
        self.fractal._maybe_make_new_plotter(backend)
        self.fractal.plotter.plot_generation(self, **kwargs)

    def grow(self, in_place=False):
        if in_place:
            generation = self
        else:
            generation = deepcopy(self)

        next_points = generation._next_points()
        generation._points = next_points
        generation._order += 1
        return generation

    def _next_points(self):
        point_pairs = (self._evolve(p) for p in self._points)
        return list(chain.from_iterable(point_pairs))

    @staticmethod
    def _evolve(point):
        i, x = point
        if x%2 == 0:
            return [[2*i, 2*x], [2*i+1, 2*x+1]]
        else:
            return [[2*i, 2*x+1], [2*i+1, 2*x]]
