import csv;
from Geometry import Point2D;
from Geometry import Vector2D;
from subdomain import subdomain;
from collections import deque;

class ReadCSV:
    def __init__(self,path):
        self.path = path;

    def _readCoordsFromRow(self,nNodes,row):
        coords = deque();
        for i in range(0,nNodes):
            x = float(row[i*2+1]);
            y = float(row[i*2+2]);
            coords.append(Point2D(x,y));
        return coords

    def _readDispFromRow(self,nNodes,row):
        displacement = deque();
        for i in range(0,nNodes):
            ux = float(row[nNodes*2+2 + i*2+1]);
            uy = float(row[nNodes*2+2 + i*2+2]);
            displacement.append(Vector2D(ux,uy));
        return displacement;

    def _readSubdomainFromRow(self,row):
        nNodes = int(row[0]);
        # read polygon
        coords = self._readCoordsFromRow(nNodes,row);
        # read scaling center
        x = float(row[nNodes*2+1]);
        y = float(row[nNodes*2+2]);
        SC = Point2D(x,y);
        # read disp
        displacement = self._readDispFromRow(nNodes,row);
        # read error
        error = float(row[-1]);
        return subdomain(coords,SC,displacement,error);

    def _readHeader(self,row):
        nSubdomains = int(row[0]);
        globalError = float(row[3]);
        return {"nSubdomains":nSubdomains, "error":globalError};

    def getTrainData(self):
        with open(self.path) as csvFile:
            reader = csv.reader(csvFile, delimiter=',');
            isFirstRow = True;
            subdomains=deque();
            for row in reader:
                if isFirstRow is False:
                    subdomain = self._readSubdomainFromRow(row);
                    subdomains.append(subdomain);
                else:
                    header = self._readHeader(row);
                    isFirstRow = False;
            return subdomains,header;
    
