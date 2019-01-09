import sys
import os.path
import math
import numpy as np

from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

import matplotlib.pyplot as plt

d = np.linspace(0, 2, 100)

plt.plot(d, d, label='linear')
plt.plot(d, d**2, label='quadratic')
plt.plot(d, d**3, label='cubic')

plt.xlabel('x label')
plt.ylabel('y label')

plt.title("Simple Plot")

plt.legend()

plt.show()



if os.path.isfile("data.csv"):
    fd = open("data.csv", "r+")
    print ("data found")
else:
    print ("The file data is not found")
    exit()

data = fd.readlines()
parsedData = []
for line in data:
    if "km,price" in line:
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

print (parsedData)

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

print (a)
print (b)

r2 = sum(Sigxy) / math.sqrt(sum(Sigx) * sum(Sigy))
print (r2)
