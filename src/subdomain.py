from Geometry import Polygon;


class subdomain:
    def __init__(self,coords,center,displacement,err):
        # coords        array of point2d
        # center        a point2d
        # displacement  array of vector2d
        # err           float 
        self.polygon = Polygon(coords);
        self.center = center;
        self.displacement = displacement;
        self.err = err;

    # def _getAngle():



