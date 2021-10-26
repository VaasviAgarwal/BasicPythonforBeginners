#menu driven program
#writing a program to understand the use of conditional statements
print("Enter the part number you want to be executed")
print("Part 1) finding the greater number out of the two")
print("Part 2) seeing if the number is +ve, -ve or zero")
print("Part 3) check whether the number enterd by the user is divisible by 5 and 11")
print("Part 4) check whether the number entered by the user is a leap year or not")
print("Part 5) finding out if a number is even or odd")
choice = int(input("Enter your choice : "))

if(choice == 1):
    #accepting numbers a and b and assuming that the user will enter an integer value
    a=int(input('Enter the first number : '))
    b=int(input('Enter the second number : '))
    if (a>b) :
        print(a,"is greater than",b)
    elif (a<b) :
        print(b,"is greater than",a)
    else :
        print("Both numbers are equal")
    
elif(choice == 2):
    #assuming that the user enters an int value
    n=int(input("Enter an integer number : "))
    if (n>0) :
        print(n,"is a positive number")
    elif (n<0) :
        print(n,"is a negative number")
    else :
        print(n,"is zero")

elif(choice == 3) :
    #assuming that the user enters a positive integer m
    m=int(input("Enter a postive number  : "))
    if (m%5==0)  or (m%11==0) :
        if(m%5==0) and (m%11==0):
            print(m,"is divisible by both 5 and 11")
        elif(m%5==0):
            print(m,"is only divisible by 5 and not 11")
        else:
            print(m,"is only divisible by 11 and not 5")
    else :
        print(m,"is neither divisible by 11 not 5")

elif(choice == 4) :
    #assuming user enters a positive whole number as the year
    year=int(input("Enter the year you want to check for : "))
    if(year%4==0 and year%100!=0) or (year%400==0):
        print(year,"was a leap year")
    else:
        print(year,"was not a leap year")

elif(choice == 5) :
    #assuming the user enters an integer value
    n=int(input("Enter a number : "))
    if(n%2==0):
        print(n,"is an even number")
    else:
        print(n,"is an odd number")
else :
    print("your choice is invalid")

