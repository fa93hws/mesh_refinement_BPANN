from src.ReadCSV import ReadCSV;
import numpy;
import math;
import matplotlib.pyplot as ploter;
from sklearn.neural_network import MLPRegressor;
from sklearn.neural_network import MLPClassifier;
from sklearn.neighbors import KNeighborsClassifier;

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
            if len(self.subdomains[i].polygon.nodes) is not 4:
                continue;
            features = [self.areas[i],self.dispDiffs[i]];
            x.append(features);
            y.append(self.improves[i]);
        return x,getRefined(y);
    def plotCls2D(self,x,y):
        rx=[];ry=[];bx=[];by=[];
        for i in range(0,len(y)):
            if (y[i] == 1):
                rx.append(x[i][0]);
                ry.append(x[i][1]);
            else:
                bx.append(x[i][0]);
                by.append(x[i][1]);
        # print(rx);
        # print(ry);
        ploter.plot(rx,ry,'ro');
        ploter.plot(bx,by,'bo');
        ploter.show();


def getRefined(err):
    err = numpy.array(err);
    idx = numpy.argsort(err);
    thresholdIdx = idx[math.floor(len(idx)*0.5)];
    threshold = err[thresholdIdx];
    idx1 = err > threshold;
    idx0 = ~idx1;
    err[idx1] = 1;
    err[idx0] = 0;
    return err;

# reading data from csv
csvFile = ReadCSV("./train_data/hole_in_plate.csv");
subdomains, header = csvFile.getTrainData();
collection = SubDomainCollection(subdomains,header);
trainX,trainY = collection.extractTrainData();
collection.plotCls2D(trainX,trainY);
# build neural network
# regressor = KNeighborsClassifier(n_neighbors=3);
regressor = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1);
# trainX,trainY = collection.extractTrainData();
trainX,trainY = collection.extractTrainData(mode='odd');
# train
regressor.fit(trainX,trainY);
# fit test data
predictX,correctY = collection.extractTrainData(mode='even');
predictY = regressor.predict(predictX);
score = regressor.score(predictX,correctY);
print(score);
# plot result
# ploter.plot(predictY,'r');
# ploter.plot(correctY,'b');
# ploter.legend(['predict','correct']);
# ploter.show();

# print("done");
