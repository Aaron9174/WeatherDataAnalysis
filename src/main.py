import meteostat
import math
from enum import Enum
from datetime import datetime

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

class TimeFrame:
    __END_DAY_SENTINAL = -1
    __DAYS_IN_REG_MONTH = 31
    __DAYS_IN_SPECIAL_MONTH = 30
    __DAYS_IN_FEBRUARY = 28

    def __init__(self, startYear, startMonth, endYear, endMonth, startDay=1, endDay=__END_DAY_SENTINAL):
        self.startYear = startYear
        self.startMonth = startMonth
        self.startDay = startDay
        self.endYear = endYear
        self.endMonth = endMonth
        if endDay == TimeFrame.__END_DAY_SENTINAL:
            self.endDay = self.__getMonthEndDay()        
        else:
            self.endDay = endDay
    
    def getStartDate(self):
        return datetime(self.startYear, self.startMonth, self.startDay)
    
    def __getMonthEndDay(self, month):
        match month:
            case Month.JANUARY:
                return TimeFrame.__DAYS_IN_REG_MONTH
            case Month.FEBRUARY:
                if self.endYear
                return TimeFrame.__DAYS_IN_FEBRUARY


class FullRangeTempResult:
    def __init__(self, missingTotal, totalAverage):
        self.dailyDataMissingTotal = missingTotal
        self.totalAverageTempC = totalAverage

# Constants
PALM_BAY_FL_LOC = meteostat.Point(28.03, -80.59)
OLDEST_DATE = datetime(1945, 1, 1)
NEWEST_DATE = datetime(2024, 9, 30)
DAYS_IN_LEAP_YEAR_FEBRUARY = 29
DAYS_IN_LEAP_YEAR = 366
DAYS_IN_YEAR = 365

# Set the start and end dates
# NOTE: 1945 is the furthest dates to go back
timeframe = TimeFrame(OLDEST_DATE, NEWEST_DATE)

# Fetch daily weather data
dailyWeatherData = meteostat.Daily(PALM_BAY_FL_LOC, timeframe.startDate, timeframe.endDate)
dailyWeatherData = dailyWeatherData.fetch()

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return False

def calculateAverageMonthlyTempC(dailyWeatherData):
    averageTempSum = 0.0
    totalMissingDataInDays = 0
    for dailyAvgTemp in dailyWeatherData["tavg"]:
        if math.isnan(dailyAvgTemp):
            totalMissingDataInDays += 1
        else:
            averageTempSum += dailyAvgTemp
    
    return FullRangeTempResult(totalMissingDataInDays, averageTempSum / len(dailyWeatherData.index))

totalAvgResult = calculateAverageMonthlyTempC(dailyWeatherData)

print(dailyWeatherData)
print("=========================================")
print("Average monthly temp: ", totalAvgResult.totalAverageTempC)
print("Total missing days: ", totalAvgResult.dailyDataMissingTotal)