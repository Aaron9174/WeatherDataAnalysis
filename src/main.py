import meteostat
import matplotlib.pyplot as plt
from enum import Enum
from datetime import datetime
import numpy as np

DAYS_IN_REG_MONTH = 31
DAYS_IN_SPECIAL_MONTH = 30
DAYS_IN_FEBRUARY = 28
DAYS_IN_LEAP_YEAR_FEBRUARY = 29

class Month(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5 
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

PALM_BAY_FL_LOC = meteostat.Point(28.03, -80.59)
NEW_YORK_FL_LOC = meteostat.Point(40.71, 74)
yearsList = range(2000, 2023)

testData = []
for year in yearsList:
    startDate = datetime(year, 1, 1)
    endDate = datetime(year, 12, 31)
    data = meteostat.Daily(PALM_BAY_FL_LOC, startDate, endDate)
    data = data.fetch()
    avgYearlyTemp = data["tavg"].mean(skipna=True)
    testData.append(avgYearlyTemp)

plt.plot(yearsList, testData)
plt.xticks(np.arange(2000, 2024, 2))
plt.xlabel("Years")
plt.ylabel("Temperature (C)")
plt.title("Average Temperature Of Palm Bay")
plt.show()
    
