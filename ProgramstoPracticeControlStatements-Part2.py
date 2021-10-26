#assignment 9 to practice control statements
#menu driven program
#using while loop which will terminate if the user chooses to enter 0
#assuming that the user enters correct datatype everytime he is asked to enter something
#i will be the loop/control variable in all cases
print("Enter 10 to find and print the first and last digits of a number from right to left")
print("Enter 11 find and the print the sum of the first and last digit of a number")
print("Enter 12 to take two numbers from user and swap the numbers")
print("Enter 13 to swap the first and last digits of a number")
print("Enter 14 to calculate sum of the digits of a number")
print("Enter 15 to calculate product of the digits of a number")
print("Enter 16 to print the reverse of a number")
print("Enter 17 to check whether a number is palindrome or not")
print("Enter 0 to terminate the program and stop the choice option")
choice = int(input("Enter your choice : "))

#starting a while loop on the condition that the users does not choose 0 as their choice
while choice != 0 :

    #to print the first and last digits of a number from right to left
    if choice == 10 :
        n = int(input("Enter the number : "))
        if n != 0 :
            if n < 0 :
                a = n - (2*n)
            else :
                a = n
            count = 0
            #storage to use it finally even if the number is -ve
            s=a
            while a > 0 :
                count = count + 1
                a = a//10
            if count == 1 :
                print("The first and last digits of the number are same (as it is a single digit number). It is",s)
            else :
                print("First digit of the number is",(s%10))
                print("Last digit of the number is",(s//(10**(count-1))))
        else :
            print("The first and last digits of the number are same (as it is a single digit number). It is 0")

    #to print the sum of the first and last digit of the number entered by the user
    elif choice == 11 :
        n = int(input("Enter the number : "))
        if n != 0 :
            #storage is an alibi for incase the number is a single digit or need to be worked on later as +ve
            if n < 0 :
                #making a positive so that the number can be worked with
                a = n - (2*n)
                storage = a
            else :
                a = n
                storage = a
            count = 0
            while a > 0 :
                count = count + 1
                a = a//10
            if count == 1 :
                print("The first and last digits of the number are equal as it is a single digit number")
                print("Therefore the sum would be double of the number which is equal to",(storage*2))
            else :
                firstdigit = storage%10
                lastdigit = (storage//(10**(count-1)))
                print("The sum of the first and last digits is",(firstdigit + lastdigit))
        else :
            print("The number entered is 0 therefore the sum will also be 0")

    #to swap two numbers
    elif choice == 12 :
        a = int(input("Enter number a : "))
        b = int(input("Enter number b : "))
        #temp stores the number temporarily for swapping
        temp = a
        a = b
        b = temp
        print("After swapping a is",a,"and b is",b)

    #to swap the first and last digits of a number
    elif choice == 13 :
        n = int(input("Enter the number : "))
        if n!=0 :
            #a to user it as a number on which operations can be performed
            #storage to store it with another copy if needed in the future
            if n < 0 :
                a =  n - (2*n)
                storage = a
            else :
                a = n
                storage = a
            count = 0
            while a > 0 :
                count = count + 1
                a = a//10
            if count == 1 :
                print("The number will remain same as it is a single digit number")
                print("It will be",n)
            else :
                firstdigit = storage%10
                lastdigit = storage//(10**(count-1))
                #calculation of middle part will be in two steps
                middlepart = storage//10
                middlepart = middlepart%(10**(count-2))
                #to put the sign of the number if it is a negative number
                if n < 0 :
                    sign = '-'
                else :
                    sign = ''
                #different part for double digit numbers as they wont have middle parts
                if count == 2 :
                    print(sign,firstdigit,lastdigit,sep='')
                else :
                    print(sign,firstdigit,middlepart,lastdigit,sep='')
        else :
            print("The number will remain same as it is a single digit number")
            print("It will be 0")

    #to calculate the sum of digits of a number
    elif choice == 14 :
        n = int(input("Enter a number : "))
        if n==0 :
            print("The sum is 0")
        else :
            #a to store the number for operations to be performed
            if n < 0 :
                a = n - (n*2)
            else :
                a = n
            # s to store the sum
            s = 0
            while a > 0 :
                s = s + (a%10)
                a = a//10
            print("The sum is",s)

    #to calculate the product of the digits of a number
    elif choice == 15 :
        n = int(input("Enter a number : "))
        if n==0 :
            print("The product is 0")
        else :
            #a to store the number for operations to be performed
            if n < 0 :
                a = n - (n*2)
            else :
                a = n
            # p to store the product
            p = 1
            while a > 0 :
                p = p * (a%10)
                a = a//10
            print("The product is",p)

    #to print the reverse of a number if the number is -ve print reverse no with same sign
    elif choice == 16 :
        n = int(input("Enter a number : "))
        if n==0 :
            print("The reverse is 0")
        else :
            #a to store the number on which operations has to be performed
            if n < 0:
                a = n - (n*2)
            else :
                a = n
            #r to store the reverse of the number
            reverse = 0
            while a > 0 :
                reverse = (reverse*10) + (a%10)
                a = a//10
            #if number is smaller than 
            if n < 0 :
                r = -reverse
            else :
                r = reverse
            #printing the answer
            print("The reverse of the number is",r)

    #to check if the number entered by the user is a palindrome number
    elif choice == 17 :
        n = int(input("Enter a number : "))
        if n==0 :
            print("The reverse is 0")
        else :
            #a to store the number on which operations has to be performed
            if n < 0:
                a = n - (n*2)
            else :
                a = n
            #r to store the reverse of the number
            r = 0
            while a > 0 :
                r = (r*10) + (a%10)
                a = a//10
            if n < 0 :
                r = -r
            if r == n :
                print("The number is a palindrome number")
            else :
                print("The number is not a palindrome number")

    #if the choice is an invalid number then message to be shown
    else :
        print("Invalid entry : Choice was not given")

    #printing a symbol to distinguish everytime the loop runs again
    print("---------------------------------------------------------------------------------------------------------------------------")

    #accepting choice again so that the loop can be rerun
    print("Enter 10 to find and print the first and last digits of a number from right to left")
    print("Enter 11 find and the print the sum of the first and last digit of a number")
    print("Enter 12 to take two numbers from user and swap the numbers")
    print("Enter 13 to swap the first and last digits of a number")
    print("Enter 14 to calculate sum of the digits of a number")
    print("Enter 15 to calculate product of the digits of a number")
    print("Enter 16 to print the reverse of a number")
    print("Enter 17 to check whether a number is palindrome or not")
    print("Enter 0 to terminate the program and stop the choice option")
    choice = int(input("Enter your choice : "))

#if user entered 0 then will be moved out of the loop
print("Program terminated as you entered 0")



