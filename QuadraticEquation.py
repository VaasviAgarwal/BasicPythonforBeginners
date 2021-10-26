#assuming that the user enters correct datatypes in each case
#importing math library
import math
#program for solving a quadratic equation
#accepting a b and c for ax^2 + bx + c = 0
a,b,c= float(input("Enter a : ")), float(input("Enter b : ")), float(input("Enter c : "))
#find discriminant
dis = (b*b) - (4*a*c)
if dis < 0 :
    print("The roots will be imaginary and cannot be calculated")
else :
    #finding root of equation by using math library functin for finding under root of discriminant
    ur = math.sqrt(dis)
    root1= (-b + ur)/2
    root2= (-b - ur)/2
    #rounding off the answers to 2 decimal places each
    root1 = round(root1, 2)
    root2 = round(root2, 2)
    #printing the answers
    print("The roots of the equation are",root1,"and",root2)
