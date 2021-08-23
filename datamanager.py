# Python Data management file
import requests
import urllib3
import json


def printResults(data):
    theJSON = json.loads(data)

    if "title" in theJSON["metadata"]:
        print(theJSON["metadata"]["title"])

    count = theJSON["metadata"]["count"]
    print(str(count) + " events recorded")

    for i in theJSON["features"]:
        print(i["properties"]["place"])
    print("---------------\n")

    for i in theJSON["features"]:
        if i["properties"]["mag"] <= 2.0:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
    print("---------------\n")


def main():
    webUrl = requests.get("https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson")
    print("result code: " + str(webUrl.status_code))
    if webUrl.status_code == 200:
        data = webUrl.content
        printResults(data)
    else:
        print("Received error")


if __name__ == "__main__":
    main()
