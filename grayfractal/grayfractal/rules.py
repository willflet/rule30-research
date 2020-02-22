""" Rules for growing fractals. """

from abc import ABC, abstractmethod
from itertools import chain
from .fractal import Generation


class Rule(ABC):
    """ Abstract base class for fractal growth rules.

    A rule defines the new generation as a function of the old generation,
    as well as capturing the scaling effect this produces.
    """

    def __init__(self):
        pass

    @property
    @abstractmethod
    def scaling(self):
        """ The scaling operation from generation to generation. """

    @property
    @abstractmethod
    def base_generation(self):
        """ The base case (order 0) generation for this rule. """

        default_base_generation = Generation(
            rule=self,
            order=0,
            points=[[0,0]]
        )
        return default_base_generation

    @abstractmethod
    def apply(self, generation):
        """ Return the next generation. """


class GrayCode(Rule):
    """ For each point [i,x], x is the Gray code of i.

    Results in:
        [[0,0], [1,1], [2,3], [3,2], [4,6], [5,7], [6,5], [7,4], ...]
    """

    def __init__(self):
        pass

    @property
    def scaling(self):
        return lambda x: x/2

    @property
    def base_generation(self):
        return super().base_generation

    def apply(self, generation, in_place=False):

        point_pairs = (self._evolve(p) for p in generation._points)
        new_points = list(chain.from_iterable(point_pairs))

        if in_place:
            generation._points = new_points
            generation._order += 1
            return generation
        else:
            return Generation(
                rule=self,
                order=generation.order + 1,
                points=new_points,
                fractal=generation.fractal
            )

    @staticmethod
    def _evolve(point):
        i, x = point
        if i%2 == 0:
            return [[2*i, 2*x], [2*i+1, 2*x+1]]
        else:
            return [[2*i, 2*x+1], [2*i+1, 2*x]]


class InverseGrayCode(Rule):
    """ For each point [i,x], i is the Gray code of x.

    Results in:
        [[0,0], [1,1], [2,3], [3,2], [4,7], [5,6], [6,4], [7,5], ...]
    """

    def __init__(self):
        pass

    @property
    def scaling(self):
        return lambda x: x/2

    @property
    def base_generation(self):
        return super().base_generation

    def apply(self, generation, in_place=False):

        point_pairs = (self._evolve(p) for p in generation._points)
        new_points = list(chain.from_iterable(point_pairs))

        if in_place:
            generation._points = new_points
            generation._order += 1
            return generation
        else:
            return Generation(
                rule=self,
                order=generation.order + 1,
                points=new_points,
                fractal=generation.fractal
            )

    @staticmethod
    def _evolve(point):
        i, x = point
        if x%2 == 0:
            return [[2*i, 2*x], [2*i+1, 2*x+1]]
        else:
            return [[2*i, 2*x+1], [2*i+1, 2*x]]
