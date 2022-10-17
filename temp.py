import random
import numpy as np


# perhaps two cities try to belong to the same airport causing weirdness
def getClosestCities(cities, airports):
    closestCities = []  # this is from airports perspective
    copyOfCities = cities.copy()
    airportIndex = -1
    for i in range(0, num_air):
        c = []
        closestCities.append(c)

    while len(copyOfCities) != 0:
        current = copyOfCities.pop()
        distance = float('inf')
        cityMin = float('inf')
        # checks the distance of each city to each airport
        for i in range(0, num_air):
            distance = (((current[0] - airports[i][0]) ** 2) + ((current[1] - airports[i][1]) ** 2)) ** 0.5
            # if the distance from current city to airport i is smaller than any of the others so far, update airportIndex
            if distance < cityMin:
                cityMin = distance
                airportIndex = i

        closestCities[airportIndex].append(current)

    return closestCities


def getGradient(airports, closestCities):
    gradient = []
    gradientX = 0
    gradientY = 0
    for i in range(num_air):
        gradientX = 0
        gradientY = 0
        for j in range(0, len(closestCities[i])):
            gradientX += 2 * (airports[i][0] - closestCities[i][j][0])
            gradientY += 2 * (airports[i][1] - closestCities[i][j][1])
        p = (gradientX, gradientY)
        gradient.append(p)

    return gradient


def getObjectiveValue(airports, closestCities):
    objectiveValue = 0
    for i in range(num_air):
        for j in range(0, len(closestCities[i])):
            objectiveValue += (((airports[i][0] - closestCities[i][j][0]) ** 2) + (
                        (airports[i][1] - closestCities[i][j][1]) ** 2))
    return objectiveValue


num_city = 100
num_air = 3
num_center = 5
sigma = 0.1
cities = set()
airports = []
test = set()

for i in range(num_center):
    x = random.random()
    y = random.random()
    xc = np.random.normal(x, sigma, num_city // num_center)
    yc = np.random.normal(y, sigma, num_city // num_center)
    cities = cities.union(zip(xc, yc))
# cities = {(0.12749879653571908, 0.6968079661945297), (0.04334400094239524, 0.8672516675013009), (0.9549714535388739, 0.8490430806134133), (0.6076484189819049, 0.3928240708035462), (-0.05302422348773289, 0.8110443471621493), (0.9112072995506936, 0.8488188420982047), (0.009512508949510551, 0.8627091096927669), (0.9585446518444818, 0.66425348725911), (0.6220642948940205, 0.7710299058223268), (0.7317306923867486, 0.6770172811982382), (0.9807941461571041, 0.7404244751120825), (-0.07431788687190928, 0.6988001138888775), (0.8204238104021716, 0.5167571664335583), (0.7138727660402879, 0.8666323782762733), (0.03260415439201369, 0.7901571420931226), (0.5833305300082358, 0.6812893756638544), (0.6559613306349125, 0.4528026326711002), (0.6932549040143912, 0.31775586003579437), (0.6765475167725085, 0.5333225059887904), (0.6207771080276123, 0.6113098426201622), (-0.046094203200001516, 0.8182924761060287), (0.5303681951775138, 0.3253357954780491), (0.8215048137955546, 0.3787186215733251), (0.5941191666769438, 0.3044695438760631), (0.7804215980529708, 0.2815951310317321), (0.618155621989224, 0.32464194787599404), (0.6256808475560347, 0.3852670212630512), (0.7541905550361667, 0.3434777193849195), (0.8383494441971384, 0.40354474453674444), (-0.0999613978110877, 0.7223453565545448), (0.8029137374314641, 0.20979441540436755), (0.9578772405828608, 0.9475993419034321), (0.03239591904552642, 0.6918723887183038), (0.6318814364887035, 0.6046479667531498), (0.8609032226115312, 0.3066540036397349), (1.0224096533619298, 0.4617808637810295), (0.9941403593389003, 0.7627349372140043), (0.9141453340050263, 0.602546543661679), (-0.014259843172647835, 1.1122552619895338), (0.040813985732560856, 0.8057950035258797), (0.7077404226177519, 0.7640371547692082), (0.897371568219367, 0.7645480667661894), (0.7861497539225237, 0.26956025894618507), (0.6255170480516872, 0.2596020394017343), (0.8490631656544902, 0.5993511221782248), (0.7962760588790618, 0.4016867584212349), (0.8215027460656176, 0.5290473112377848), (0.6733852012768595, 0.1819973734085041), (0.038287705956534385, 0.750589486080474), (-0.12829415494746024, 0.6996318631686285), (0.6005622909008117, 0.8418933204888323), (0.7972778570698116, 0.7806121695687605), (0.07411574923849629, 0.8862599909703817), (0.8565906867172199, 0.38382086889700284), (0.7153483558763767, 0.7302048772278361), (0.9409679335097777, 0.5969275787927213), (0.6968248678874157, 0.5124674294528475), (0.003805400649383627, 0.919206381438272), (0.6876448015206917, 0.5925730889660284), (0.8635896581685638, 0.8349728386588063), (0.8510726102963683, 0.5237022476369737), (0.8746209795599008, 0.49754609217869145), (0.6881577609140709, 0.6297226175089612), (0.893884441831339, 0.8479363968049946), (0.12532275658534214, 0.6725642899460547), (0.7518785017240568, 0.7535432728735116), (0.5277762110896161, 0.7767999947068168), (0.9087424956622325, 0.7494529519793379), (0.6096095156040353, 0.7429872568276215), (0.846711508727759, 0.8431307582065137), (0.7319596394906063, 0.4409525909182127), (0.6229148864924439, 0.7855599904896772), (0.8711870667478759, 0.754958656419504), (0.670588030705596, 0.33229789726582915), (0.669794632499406, 0.6109206889888424), (0.6629778943397764, 0.7946740738416331), (0.9937829174360451, 0.7692023919017931), (0.8340965260234351, 0.8590072442808303), (0.2121968034463349, 0.8246898509019134), (0.8904642958313846, 0.6425982525904642), (0.8907862605438169, 0.8570861037869474), (0.6981738790498917, 0.5767203242070924), (1.127430278152575, 0.6320400791210408), (-0.10478561083583166, 0.8344948674978879), (1.0765162474685561, 0.7719405785617869), (0.6148893017214849, 0.4392844858318163), (0.9771413419576568, 0.7554159425947934), (0.9763160682222493, 0.671102018747522), (0.8261266905492304, 0.7835316120459994), (0.8190436281743749, 0.6164853465042754), (0.755557255714892, 0.5294524552631779), (-0.045245605170151734, 0.886549929172675), (0.6697870717017297, 0.5020641205060423), (0.6754439645816747, 0.5432666815325764), (0.9053127894786561, 0.3909598257900006), (-0.035309917529233736, 0.6998405827061813), (0.8651564069093732, 0.48300347058582166), (0.6702197289361559, 0.49746237243335106), (0.773534893571019, 0.9472178020265412), (0.8163022520221305, 0.8156303833829986)}
for i in range(num_air):
    x = random.random()
    y = random.random()
    airports.append((x, y))
# airports = [(0.9504067726259473, 0.16688608685502493), (0.8000285334691492, 0.043655082036591075), (0.972925995523019, 0.7214267864171258)]


closestCities = getClosestCities(cities, airports)
gradient = getGradient(airports, closestCities)
objectiveValue = getObjectiveValue(airports, closestCities)
print("airports: " + str(airports))
print("cities " + str(cities))
print("Objective Value " + str(objectiveValue))
print("Gradient: " + str(gradient))

numberOfLoops = 0
# main loop will start here
endVal = 0.0001
while abs(gradient[0][0]) > endVal or abs(gradient[0][1]) > endVal or abs(gradient[1][0]) > endVal or abs(
        gradient[1][1]) > endVal or abs(gradient[2][0]) > endVal or abs(gradient[2][1]) > endVal:

    numberOfLoops += 1
    # Not sure if i should recalculate this every time
    closestCities = getClosestCities(cities, airports)
    gradient = getGradient(airports, closestCities)
    for i in range(0, num_air):
        airports[i] = (airports[i][0] - (gradient[i][0] * 0.01), airports[i][1] - (gradient[i][1] * 0.01))

    objectiveValue = getObjectiveValue(airports, closestCities)

import matplotlib.pyplot as plt

zip_cities = zip(*cities)
plt.scatter(*zip_cities, marker='+', color='b', label='Cities')
zip_airs = zip(*airports)
plt.scatter(*zip_airs, marker='*', color='r', s=100, label='Airports')
plt.legend()
plt

print("airports: " + str(airports))
print("Objective Value " + str(objectiveValue))
print("Gradient: " + str(gradient))
print("it took " + str(numberOfLoops) + " loops to complete")
# [airport number][city number][x or y cord]
# closestCities[0][0][0]
