import sys
import os.path

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

print parsedData

m = len(parsedData)
i = 0
t0 = 0
t1 = 0
alpha = 0.0001 / float(sum([it[0] for it in parsedData]))
while (i < 100000):
    tmp0 = t0
    tmp1 = t1
    t0 = tmp0 - alpha * sum([ ( it[0] * tmp1 + tmp0 - it[1] ) for it in parsedData ]) / m
    t1 = tmp1 - alpha * sum([ ( ( it[0] * tmp1 + tmp0 - it[1] ) * it[0] ) for it in parsedData ]) / m
    i += 1
    
print (t1)
print (t0)

