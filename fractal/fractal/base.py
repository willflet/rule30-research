""" Mathematical objects describing growth of a cyclic binary fractal. """

from copy import deepcopy
from itertools import chain
from .plotting import FractalPlotter

class Fractal(object):
    """ A collection of fractal generations, with global properties. """

    def __init__(self):
        """ Make a base case fractal segment. """
        self._generations = [Generation()]
        #self._plotter = FractalPlotter(self)

    @property
    def order(self):
        return len(self._generations) - 1

    @property
    def generations(self):
        return self._generations

    def grow(self):
        new_generation = self.generations[-1].grow(in_place=False)
        self._generations.append(new_generation)

    # def plot(self, *args, **kwargs):
    #     self._plotter.plot(*args, **kwargs)


class Generation(object):
    """ A single generation of the fractal. """

    def __init__(self):
        self._points = [[0,0]]

    @property
    def order(self):
        return len(self._points) - 1

    @property
    def points(self):
        return self._points + [self._end_point]

    @property
    def _end_point(self):
        return [2**self.order, 2**self.order]

    def grow(self, in_place=False):
        if in_place:
            generation = self
        else:
            generation = copy.deepcopy(self)

        new_points = generation._next_points()
        generation._points = new_points
        return generation

    def _next_points(self):
        return list(chain(self._evolve(p) for p in self._points))

    @staticmethod
    def _evolve(point):
        i, x = point
        if x%2 == 0:
            return [[2*i, 2*x], [2*i+1, 2*x+1]]
        else:
            return [[2*i, 2*x+1], [2*i+1, 2*x]]
