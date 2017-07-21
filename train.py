import csv;
from collections import deque;
from Point2D import Point2D;
from subdomain import subdomain;

def readPolygonFromRow(row):
    nNodes = int(row[0]);
    for iPolygon in range(0,nNodes):


def readPolygonFromCSV(path):
    with open(path) as csvFile:
        reader = csv.reader(csvFile, delimiter=',');
        for row in reader:
            readPolygonFromRow();

readPolygonFromCSV("./train_data/hole_in_plate.csv");

