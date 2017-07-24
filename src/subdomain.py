from collections import deque;
from src.Geometry import Polygon;
from src.Geometry import Vector2D;
import numpy;
import math;

class subdomain:
    def __init__(self,coords,center,displacement,dispIndicator,stressIndicator,refined):
        # coords        array of point2d
        # center        a point2d
        # displacement  array of vector2d
        # refined       1=refined, 0=no
        # 
        self.polygon = Polygon(coords,center);
        self.center = center;
        self.displacement = displacement;
        self.refined = refined;
        self.dispIndicator = dispIndicator;
        self.stressIndicator = stressIndicator;
        self.angles = self._getAngles();
    def _getAngles(self):
        angles = deque();
        nodes = numpy.array(self.polygon.nodes);
        edges = numpy.column_stack((nodes,numpy.roll(nodes,1)));
        for [pt1,pt2] in edges:
            vec1 = Vector2D(pts=[pt1,self.center]);
            vec2 = Vector2D(pts=[pt2,self.center]);
            cosAngle = vec1 * vec2 / vec1.getNorm() / vec2.getNorm();
            angle = math.acos(cosAngle);
            angles.append(angle);
        return angles;
    def getAngleRatio(self):
        maxAngle = 0.0;
        minAngle = math.pi
        for angle in self.angles:
            if angle > maxAngle:
                maxAngle = angle;
            elif angle < minAngle:
                minAngle = angle;
        return minAngle/maxAngle;
    def getMaxDispDiff(self):
        maxDiff = 0;
        for i in range(0,len(self.displacement)-1):
            for j in range(i+1,len(self.displacement)):
                vec1 = self.displacement[i];
                vec2 = self.displacement[j];
                diff = (vec1 - vec2).getNorm();
                dist = self.polygon.nodes[i].distanceTo(self.polygon.nodes[j]);
                diff /= dist;
                if diff > maxDiff:
                    maxDiff = diff;
        return maxDiff;