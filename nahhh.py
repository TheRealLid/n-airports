import random
import numpy as np

num_city = 100
num_air = 3
num_center = 5
sigma = 0.1
cities = set()
airports = []

#generation of random cities
for i in range(num_center):
    x = random.random()
    y = random.random()
    xc = np.random.normal(x, sigma, num_city//num_center)
    yc = np.random.normal(y, sigma, num_city//num_center)
    cities = cities.union(zip(xc, yc))

#generation of random airports
for i in range(num_air):
    x = random.random()
    y = random.random()
    airports.append((x,y))

def closestCitySets(cities, airports):
    #find the sets of cities and their closest airport
    dup_set = cities.copy() #copy of the set of cities
    c0 = set()   #sets of cities with the closest airport being a0, a2, or a3
    c1 = set()
    c2 = set()
    while len(dup_set)  != 0: #as long as the duplicate set has emelents
        temp = dup_set.pop()  #temp will hold the current city position
        tempDist = 0          #used to hold the calculated squared distance from the given city to an airport
        smlDist = float('inf')#used to hold the current shortest distance from the city to a given airport
        clsAirPrt = -1        #used to hold the current airport that is the closest to a city
        for x in range(3):
            tempDist = (airports[x][0] - temp[0])**2 + (airports[x][1] - temp[1])**2   #sqrd distance calc
            if tempDist < smlDist:   #if the found distance is shorter than the stored shortest distance then make it the new shortest and record the airport
                smlDist = tempDist
                clsAirPrt = x
        if clsAirPrt == 0:      #assign the city to its closest airport
            c0.add(temp)
        elif clsAirPrt == 1:
            c1.add(temp)
        elif clsAirPrt == 2:
            c2.add(temp)
        else:                   #flags an error
            print("closest airport error")
    return c0,c1,c2   #returns sets of cities

def gradient(c0,c1,c2, airports):
    gradient = [0,0,0,0,0,0] #list of the gradient where each index is x1, y1, ..., x2, y2
    listOfCities = [c0,c1,c2]
    for x in range(3):
        for y in listOfCities[x]:
            gradient[2*x] += 2*(airports[x][0] - y[0])      #x value calc
            gradient[2*x + 1] += 2*(airports[x][1] - y[1])  #y value calc
    return gradient

def getObjVal(c0, c1, c2, airports):
    cityList = [c0, c1, c2]
    res = 0
    for i in range(num_air):
        for city in cityList[i]:
            res += (airports[i][0] - city[0]) ** 2 + (airports[i][1] - city[1]) ** 2
    return res


grad = [1,1,1,1,1,1] #initial gradient values to get into the while loop
counter = 0
yVals = []
xVals = []
while abs(grad[0]) > .000001 and abs(grad[1]) > .000001 and abs(grad[2]) > .000001 and abs(grad[3]) > .000001 and abs(grad[4]) > .000001 and abs(grad[5]) > .000001: #when the gradient values are not within the predetermined range
    counter += 1
    cities0, cities1, cities2 = closestCitySets(cities, airports) #move the cities to better fit the gradient
    yVals.append(getObjVal(cities0, cities1, cities2, airports))
    xVals.append(counter)
    grad = gradient(cities0,cities1,cities2, airports) #find gradient based on city and airport positions
    for x in range(len(airports)):
        if grad[x*2] != 0 and grad[x*2+1] != 0: #if the gradient values are not zero then adjust the airport positions by the gradient value multiplied by a const value
            airports[x] = (airports[x][0] - (grad[x*2] * .0001), airports[x][1] - (grad[x*2+1] * .0001))
        elif grad[x*2] != 0:
            airports[x] = (airports[x][0], airports[x][1] - (grad[x*2+1] * .0001))
        elif grad[x*2+1] != 0:
            airports[x] = (airports[x][0] - (grad[x*2] * .0001), airports[x][1])
#print(grad) TEST STATEMENT
#print(getObjVal(c0, c1, c2, airports)) TEST STATEMENT

import matplotlib.pyplot as plt

zip_cities = zip(*cities)
plt.scatter(*zip_cities, marker='+',color='b', label='Cities')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt

plt.clf()

if len(cities0) != 0:
    zip_cities0 = zip(*cities0)
    plt.scatter(*zip_cities0, marker='+',color='b', label='Cities Closest to Airport 0')
if len(cities1) != 0:
    zip_cities1 = zip(*cities1)
    plt.scatter(*zip_cities1, marker='+',color='g', label='Cities Closest to Airport 1')
if len(cities2) != 0:
    zip_cities2 = zip(*cities2)
    plt.scatter(*zip_cities2, marker='+',color='m', label='Cities Closest to Airport 2')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt


plot2 = plt.figure(2)
plt.scatter(xVals, yVals)

plt.show()
