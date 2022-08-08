import csv

sports = open("sports.csv", "r")
try:
    render = csv.reader(sports)
    for row in render:
        for item in row:
            print(item)
        print("\n")
finally:
        sports.close()