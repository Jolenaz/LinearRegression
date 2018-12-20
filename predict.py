import sys
import os.path

if os.path.isfile("coef.txt"):
    fd = open("coef.txt", "r+")
    A = fd.readline().split(" ")
else:
    A = [0,0]

print "Enter a mileage: "

data = sys.stdin.readline()

print "The predicted value of your car is:"
print (int(float(data) * float(A[0]) + float(A[1])))
