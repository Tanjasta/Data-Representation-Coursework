# reference: https://github.com/andrewbeattycourseware/datarepresentation/blob/main/code/Topic04-apis/csodao.py

# Import needed libraries
import requests
import json

# Define the beginning and end of the API URL
urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# Define a function 
# Retrieve data and write it to the file as JSON
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

# Define a function 
# Construct the complete URL for the API request 
# Make get request + return the json response
def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

# Use getAllAsFile function to get data for the "FIQ02" dataset and save it as a JSON file
if __name__ == "__main__":
    #getAllAsFile("FIQ02")
    getAllAsFile("FIQ02")
