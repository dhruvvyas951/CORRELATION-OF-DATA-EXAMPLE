import plotly.express as px
import csv
import numpy as np

def getdatasource(data_path):
    days = []
    percent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            days.append(float(row["Days Present"]))
            percent.append(float(row["MarkPercent"]))
    return{
    "x": days,
    "y": percent
    }

def findcorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation found between days and percentage is: ", correlation[0,1])

def getdata():
    data_path=("Correlation/scor.csv")
    data_source = getdatasource(data_path)
    findcorrelation(data_source)

getdata()