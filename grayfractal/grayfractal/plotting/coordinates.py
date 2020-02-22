""" Different ways to plot the fractal. """

from abc import ABC, abstractmethod


class CoordinateSystem(ABC):
    """ Abstract base class for plot coordinate systems. """

    def __init__(self):
        pass

    @abstractmethod
    def transform(self, points):
        """ Return a canonical representation of the points in the new system. """

    @abstractmethod
    def to_cartesian(self, points):
        """ Return the (x,y) coordinates ready for plotting. """


class Cartesian2D(CoordinateSystem):
    """ Ordinary 2D Cartesian coordinates, scaled to [0,1]. """

    def transform(self, points):
        raise NotImplementedError

    def to_cartesian(self, points):
        raise NotImplementedError


class Circular(CoordinateSystem):
    """ 2D Polar coordinates. """

    def transform(self, points):
        raise NotImplementedError

    def to_cartesian(self, points):
        raise NotImplementedError


class ZOrderCurve(CoordinateSystem):
    """ The Z-order fractal. A space-filling curve."""

    def transform(self, points):
        raise NotImplementedError

    def to_cartesian(self, points):
        raise NotImplementedError
