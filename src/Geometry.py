import numpy;

class Point2D:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

class Vector2D:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;

class Polygon:
    def __init__(self,nodes):
        self.nodes = nodes;
        self.area = self._getArea();

    def _getArea(self):
        x = [pt.x for pt in self.nodes];
        y = [pt.y for pt in self.nodes];
        area = numpy.dot(x , numpy.roll(y,1));
        area -= numpy.dot(y , numpy.roll(x,1));
        area /= 2;
        return numpy.abs(area);
