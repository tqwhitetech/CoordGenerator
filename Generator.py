import csv
import random
import time
import tqdm
import os
import threading
from tqdm import tqdm
from tqdm import trange
from time import sleep

date = ["May 1 1900", "May 2 1900", "May 3 1900", "May 4 1900",
        "May 5 1900", "May 6 1900", "May 7 1900", "May 8 1900",
        "May 9 1900", "May 10 1900",]
activity = "Please wait while the scripts run ..."
animate = ["|", "/", "-", "\\"]
latitude = []
longitude = []
coordinates = {}
header = ["Lat", "Long"]
k = 0
l = 0
x = 1


def generateCoords():
    for month in tqdm(date, desc="Total Progress"):

        filename = "%s.csv" % month

        for i in trange(random.randint(7000, 10000), desc="Latitude Generation: "):
            latcoord = random.uniform(38.950, 39.107)
            latitude.append(latcoord)
            sleep(.0001)

        for j in trange(random.randint(7000, 10000), desc="Longitude Generation:"):
            longcoord = random.uniform(125.590, 125.894)
            longitude.append(longcoord)
            sleep(.0001)

''' NEEDS TO BE DICTIONARY OPTIMIZED
        for lat in latitude:
            for long in longitude:
                coordinates[lat] = long
                print(coordinates)
'''

        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerow([g for g in header])
            for row in tqdm(coordinates.items(), desc="CSV Generation"):
                writer.writerow(row)



def main():
    generateCoords()
    print("Done generating coordinates. Standby for file creation.")
    print("Done generating coordinates. Standby for file creation..")
    print("Done generating coordinates. Standby for file creation...")


if __name__ == '__main__':
    main()


