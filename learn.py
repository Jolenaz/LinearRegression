import sys
import os.path
import math
import numpy as np

from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

if os.path.isfile("data.csv"):
    fd = open("data.csv", "r+")
    print ("data found")
else:
    print ("The file data is not found,\n the file data.csv must be at the root of the program")
    exit()

data = fd.readlines()
parsedData = []
firstLine = True
xLabel = "x value"
yLabel = "y value"
for line in data:
    if firstLine is True:
        firstLine = False
        parsedLine = [item.replace("\n","") for item in line.split(",")]
        xLabel = parsedLine[0]
        yLabel = parsedLine[1]
        continue
    try:
        parsedLine = [int(item.replace("\n","")) for item in line.split(",")]
        if len(parsedLine) is not 2:
            exit()
        if parsedLine[0] < 0 or parsedLine[1] < 0:
            exit() 
        parsedData.append(parsedLine)
    except:
        print ("error at line in data parsing :")
        print (line)
        exit()

m = len(parsedData)

x = [ it[0] for it in parsedData ]
y = [ it[1] for it in parsedData ]
xy = [ (it[1] * it[0]) for it in parsedData ]
x2 = [ (it[0] * it[0]) for it in parsedData ]
xm = sum(x) / m
ym = sum(y) / m

Sigxy = [ ((it[1] - ym) * (it[0] - xm))  for it in parsedData ]
Sigx  = [ ((it[0] - xm) * (it[0] - xm))  for it in parsedData ]
Sigy  = [ ((it[1] - ym) * (it[1] - ym))  for it in parsedData ]

a = float(m * sum(xy) - sum(x) * sum(y) ) / float(m * sum(x2) - sum(x) * sum(x))
b = ym - a * xm 

r2 = sum(Sigxy) / math.sqrt(sum(Sigx) * sum(Sigy))

X = np.linspace(min(x), max(x), 1000)

plt.scatter(x, y)
plt.plot(X, a*X+b)

plt.xlabel(xLabel)
plt.ylabel(yLabel)
plt.title("Linear Reg")

plt.show()

fd = open("coef.txt", "w+")
fd.writelines(str(a) + " " + str(b))
