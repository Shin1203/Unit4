import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def distancecalc(longitudeA, latitudeA, longitudeB, latitudeB):
    longitudeA = math.radians(longitudeA)
    longitudeB = math.radians(longitudeB)
    latitudeA = math.radians(latitudeA)
    latitudeB = math.radians(latitudeB)
    x = (longitudeB - longitudeA) * math.cos((latitudeA + latitudeB) / 2)
    y = latitudeB - latitudeA
    return math.sqrt(x * x + y * y)*6371
longitudeA =  float(input().replace(',', '.'))
latitudeA = float(input().replace(',', '.'))
n = int(input())
smallestD = 0
for i in range(n):
    defib = input().split(";")


    # longitude and lattitude variables, also replace "," with "."
    longitudeB = float(defib[4].replace(',', '.'))
    latitudeB = float(defib[5].replace(',', '.'))
    # The math
    distancem = distancecalc(longitudeA, latitudeA, longitudeB, latitudeB)
   
    if distancem <= smallestD or smallestD == 0:
        smallestD = distancem
        location = defib[1]


# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr)

print(location)
