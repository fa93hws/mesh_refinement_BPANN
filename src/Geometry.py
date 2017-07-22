import numpy;
import math;
from operator import itemgetter;

class Point2D:
    def __init__(self,x,y):
        self.x = x;
        self.y = y;
    def distanceTo(self,pt):
        return Vector2D(pts=[pt,self]).getNorm();

class Vector2D:
    def _initWithCoor(self,x,y):
        self.x = x;
        self.y = y;
    def _initWithPts(self,pts):
        pt1 = pts[0];
        pt2 = pts[1];
        self.x = pt2.x - pt1.x;
        self.y = pt2.y - pt1.y;
    def __init__(self,*args, **kwargs):
        if 'pts' in kwargs:
            self._initWithPts(kwargs['pts']);
        else:
            self._initWithCoor(args[0],args[1]);
    def __sub__(self,vec):
        return Vector2D(vec.x - self.x, vec.y - self.y);
    def __mul__(self,vec):
        return self.x * vec.x + self.y * vec.y;
    def getNorm(self):
        return math.sqrt(self.x**2 + self.y**2);

class Polygon:
    def __init__(self,nodes,center):
        # nodes         array of point2d
        self.nodes = nodes;
        self._reorgnizePts(center);
        self.area = self._getArea();
    def _reorgnizePts(self,center):
        angles = [];
        for pt in self.nodes:
            direction = Vector2D(pts=[center, pt]);
            angle = numpy.arctan2(direction.y,direction.x);
            angles.append(angle);
        idx = sorted(range(len(angles)),key=lambda i:angles[i]);
        self.nodes = itemgetter(*idx)(self.nodes);
    def _getArea(self):
        x = [pt.x for pt in self.nodes];
        y = [pt.y for pt in self.nodes];
        area = numpy.dot(x , numpy.roll(y,1));
        area -= numpy.dot(y , numpy.roll(x,1));
        area /= 2;
        return numpy.abs(area);
