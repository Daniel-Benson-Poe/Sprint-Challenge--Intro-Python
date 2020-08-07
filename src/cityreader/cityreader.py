import csv
# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:

  def __init__(self, name, lat, lon):
    self.name = name  # define city name
    self.lat = lat  # define city lattitude
    self.lon = lon  # define city longitude

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []  # create empty list

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # Ensure that the lat and lon valuse are all floats
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    with open('cities.csv', newline='') as csvfile:  # open csv file
      cityreader = csv.reader(csvfile)  # instantiate new csv reader using our csv file
      next(cityreader)  # skip first row (the fields header)
      for row in cityreader:  # iterate through each row of data
        cities.append(City(row[0], float(row[3]), float(row[4])))  # append the data in each row at index 0 (name), 3 (lattitude), and 4 (longitude)
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:  # iterate through cities list
    print(c)  # print out each value in cities

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# Function to clean up the user input
def coord_cleanup(point):  # pass in point as input
  lat, lon = point.split()  # split the input (should be two values)
  lat = float(lat.strip(','))  # strip the ',' from the first value, set what remains (a number) to be a float
  lon = float(lon)  # set second value (a number) to be a float
  return lat, lon  # return the two float values

point1 = input("Type in a pair of coordinate numbers 'lattitude, longitude': ")  # Ask user for first pair of coords
point2 = input("Type in a second pair of coordinate numbers 'lattitude, longitude': ")  # Ask user for second pair of coords
lat1, lon1 = coord_cleanup(point1)  # run first input point through function
lat2, lon2 = coord_cleanup(point2)  # run second input point through function


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []
  
  # Go through each city and check to see if it falls within 
  # the specified coordinates.
  # list comprehension appending each City occurance in cities list that falls between the given coordinate square
  [within.append(city) for city in cities if (min(lat1, lat2) <= city.lat <= max(lat1, lat2)) and
    (min(lon1, lon2) <= city.lon <= max(lon1, lon2))]  

  return within
