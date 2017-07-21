import csv;
from Geometry import Point2D;
from Geometry import Polygon;
from Displacement import Displacement2D;
from subdomain import subdomain;

class ReadCSV:
    def __init__(self,path):
        self.path = path;

    def _readPolyFromRow(self,nNodes,row):
        coord = [];
        for i in range(0,nNodes):
            x = float(row[i*2+1]);
            y = float(row[i*2+2]);
            coord.append(Point2D(x,y));
        return Polygon(coord);

    def _readDispFromRow(self,nNodes,row):
        displacement = [];
        for i in range(0,nNodes):
            ux = float(row[nNodes*2+2 + i*2+1]);
            uy = float(row[nNodes*2+2 + i*2+2]);
            displacement.append(Displacement2D(ux,uy));
        return displacement;

    def _readSubdomainFromRow(self,row):
        nNodes = int(row[0]);
        # read polygon
        polygon = self._readPolyFromRow(nNodes,row);
        # read scaling center
        x = float(row[nNodes*2+1]);
        y = float(row[nNodes*2+2]);
        SC = Point2D(x,y);
        # read disp
        displacement = self._readDispFromRow(nNodes,row);
        # read error
        error = float(row[-1]);
        return subdomain(polygon,SC,displacement,error);

    def _readHeader(self,row):
        nSubdomains = int(row[0]);
        globalError = float(row[3]);
        return {"nSubdomains":nSubdomains, "error":globalError};

    def getTrainData(self):
        with open(self.path) as csvFile:
            reader = csv.reader(csvFile, delimiter=',');
            isFirstRow = True;
            subdomains=[];
            for row in reader:
                if isFirstRow is False:
                    subdomain = self._readSubdomainFromRow(row);
                    subdomains.append(subdomain);
                else:
                    header = self._readHeader(row);
                    isFirstRow = False;
            return subdomains,header;
    
