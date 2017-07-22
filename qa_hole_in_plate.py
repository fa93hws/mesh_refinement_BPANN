from src.ReadCSV import ReadCSV;




csvFile = ReadCSV("./train_data/hole_in_plate.csv");
subdomains, header = csvFile.getTrainData();
print("done");
