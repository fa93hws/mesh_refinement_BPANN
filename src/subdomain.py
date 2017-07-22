
class Displacement2D:
    def __init__(self,ux,uy):
        self.ux = ux;
        self.uy = uy;

class subdomain:
    def __init__(self,polygon,center,displacement,err):
        self.polygon = polygon;
        self.center = center;
        self.displacement = displacement;
        self.err = err;

