from ReadCSV import ReadCSV;

def calculateTotalArea(subdomains):
    totalArea = 0.0;
    for subdomain in subdomains:
        polygon = subdomain.polygon;
        area = polygon.getArea();
        totalArea += area;
    return area;

csvFile = ReadCSV("./train_data/hole_in_plate.csv");
subdomains, header = csvFile.getTrainData();
totalArea = calculateTotalArea(subdomains);
print(totalArea);
print("done");
