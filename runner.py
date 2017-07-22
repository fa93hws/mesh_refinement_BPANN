from src.ReadCSV import ReadCSV;

class SubDomainCollection:
    def __init__(self,subdomains):
        self.subdomains = subdomains;
        self.angleRatio = [sd.getAngleRatio() for sd in subdomains];
        dispDiffs = [sd.getMaxDispDiff() for sd in subdomains];
        self.dispDiffs = self._normalizeArray(dispDiffs);
        areas = [sd.polygon.area for sd in subdomains];
        self.areas = self._normalizeArray(areas);
        print();
    def _normalizeArray(self,array):
        maxValue = max(array);
        normalizedArray = [x/maxValue for x in array];
        return normalizedArray;

# def __main__():
csvFile = ReadCSV("./train_data/hole_in_plate.csv");
subdomains, header = csvFile.getTrainData();
collection = SubDomainCollection(subdomains);
print("done");
