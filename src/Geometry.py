import numpy;
import math;

class Point2D:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

class Vector2D:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    
    def getNorm(self):
        return math.sqrt(self.x**2 + self.y**2);

class Polygon:
    def __init__(self,nodes):
        # nodes         array of point2d
        self.nodes = nodes;
        self.area = self._getArea();

    def _getArea(self):
        x = [pt.x for pt in self.nodes];
        y = [pt.y for pt in self.nodes];
        area = numpy.dot(x , numpy.roll(y,1));
        area -= numpy.dot(y , numpy.roll(x,1));
        area /= 2;
        return numpy.abs(area);
