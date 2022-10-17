import random
import numpy as np

num_city = 100
num_air = 3
num_center = 5
sigma = 0.1
cities = set()
airports = []

for i in range(num_center):
    x = random.random()
    y = random.random()
    xc = np.random.normal(x, sigma, num_city // num_center)
    yc = np.random.normal(y, sigma, num_city // num_center)
    cities = cities.union(zip(xc, yc))

for i in range(num_air):
    x = random.random()
    y = random.random()
    airports.append((x, y))
airports[0] = (0.5, 0.8)

import matplotlib.pyplot as plt

print(airports)
zip_cities = zip(*cities)
plt.scatter(*zip_cities, marker='+', color='b', label='Cities')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt

previousObjFunc = 999999
objectiveFunction = 10
# main loop
for k in range(0, 20):
    objectiveFunction = 0
    # gets all of the cities cordinates into an array for easier use
    cityList = []
    for i in cities:
        cityList.append(i)

    cityToAir = [5] * num_city
    # creates a list(cityToAir) that has the index of which airport a city is closest to
    for i in range(0, num_city):
        distance = 1000
        cityMin = 1000
        for j in range(num_air):
            distance = ((cityList[i][0] - airports[j][0]) ** 2 + (cityList[i][1] - airports[j][1]) ** 2) ** 0.5
            if distance < cityMin:
                cityMin = distance
                cityToAir[i] = j

    # calculates objective function
    for i in range(0, num_city):
        for j in range(0, num_air):
            if cityToAir[i] == j:
                objectiveFunction += (
                            ((cityList[i][0] - airports[j][0]) ** 2) + ((cityList[i][1] - airports[j][1]) ** 2))
    if objectiveFunction > previousObjFunc:
      print("yup...")
        #break
    else:
        previousObjFunc = objectiveFunction

    gradientX = []
    gradientY = []
    for i in range(num_city):
        gradientX.append(((cityList[i][0] - airports[cityToAir[i]][0])) * 0.001) # THIS RIGHT HERE IS THE PROBLEM
        gradientY.append(((cityList[i][1] - airports[cityToAir[i]][1])) * 0.001)

    for i in range(0, num_city):
        for j in range(0, num_air):
            if cityToAir[i] == j:
                airports[j] = (airports[j][0] - gradientX[i], airports[j][1] - gradientY[i])

    # print(objectiveFunction)

print(airports)
print("run completed")
print(objectiveFunction)
print(cityToAir)
plt.clf()
zip_cities = zip(*cities)
plt.scatter(*zip_cities, marker='+', color='b', label='Cities')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt