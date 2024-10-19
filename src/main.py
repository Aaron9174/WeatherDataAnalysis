import meteostat
from datetime import datetime

# Define the geographical point
point = meteostat.Point(28.03, -80.59)  # Palm Bay, FL

# Set the start and end dates
start = datetime(1945, 7, 1)
end = datetime(1945, 7, 31)

# Fetch daily weather data
data = meteostat.Daily(point, start, end)
data = data.fetch()

print(data)