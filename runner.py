from src.ReadCSV import ReadCSV;
import numpy;
import math;
import matplotlib.pyplot as ploter;
from sklearn.neural_network import MLPRegressor;

class SubDomainCollection:
    def __init__(self,subdomains,header):
        globalError = header['error'];
        self.subdomains = subdomains;
        self.angleRatio = [sd.getAngleRatio() for sd in subdomains];
        dispDiffs = [sd.getMaxDispDiff() for sd in subdomains];
        self.dispDiffs = self._normalizeArray(dispDiffs);
        areas = [sd.polygon.area for sd in subdomains];
        self.areas = self._normalizeArray(areas);
        improves = [(globalError-sd.error)/globalError for sd in subdomains];
        self.improves = self._normalizeArray(improves);
    def _normalizeArray(self,array):
        maxValue = max(array);
        normalizedArray = [x/maxValue for x in array];
        return normalizedArray;
    def extractTrainData(self,mode='default'):
        x = [];
        y = [];
        for i in range(0,len(self.improves)):
            if (mode is 'odd' and i%2==0) or (mode is 'even' and i%2==1):
                continue;
            elif (self.improves[i] < 0):
                continue;
            features = [self.angleRatio[i],self.dispDiffs[i],self.areas[i]];
            x.append(features);
            y.append(self.improves[i]);
        return x,y;

# reading data from csv
csvFile = ReadCSV("./train_data/hole_in_plate.csv");
subdomains, header = csvFile.getTrainData();
collection = SubDomainCollection(subdomains,header);
# build neural network
regressor = MLPRegressor(hidden_layer_sizes=(4,),solver='lbfgs',activation='identity');
# x,y = collection.extractTrainData();
trainX,trainY = collection.extractTrainData(mode='odd');
# train
regressor.fit(trainX,trainY);
# print coefs
coes = [coef for coef in regressor.coefs_];
print(coes);
# fit test data
predictX,correctY = collection.extractTrainData(mode='even');
predictY = regressor.predict(predictX);
# plot result
ploter.plot(predictY,'r');
ploter.plot(correctY,'b');
ploter.legend(['predict','correct']);
ploter.show();

print("done");
