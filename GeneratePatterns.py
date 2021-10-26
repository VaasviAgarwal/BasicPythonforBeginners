#Program to generate and print the patterns
#menu driven for the the patterns
print("Enter 1 for this pattern \n*\n**\n***\nfor n lines")
print("Enter 2 for this pattern \n$$$$\n$     $\n$     $\n$$$$\nfor n lines")
#accepting the users choice and assuming that the user enters the correct datatype
choice = int(input("Enter your choice : "))

#generating and printing the first pattern
if choice == 1 :
    n = int(input("Enter the number of rows you want (it should be greater than 0) : "))
    #telling user that their entry was invalid as its less than one
    if n < 1 :
        print("A pattern for the number of rows you entered is not possible")
    else :
        for i in range(n) :
            #running it for less than i times so that we can print one * at the end to add a new line in end
            for j in range(i) :
                print('*',end='')
            print("*")

#generating and printing the second pattern for 5 lines
elif choice == 2 :
    for i in range(5) :
        print("$",end='')
    #print statement so that next lines are not concatinated
    print(end='\n')
    #to print the line with $ on the beginning and ending with space in between
    for i in range(3) :
        #printing the $ in the beginning
        print("$",end='')
        for j in range(7) :
            #printing the extra spaces so that it can align
            print(" ",end='')
        #printing the last dollar
        print("$")
    for i in range(5) :
        print("$",end='')

#telling that the user entered a choice that was not offered
else :
    print("The choice you enterd was not given")






    
