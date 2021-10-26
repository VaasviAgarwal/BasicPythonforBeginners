n = int(input("Enter the number of rows you want (it should be greater than 0) : "))
if n > 1 :
    #to print the first line
    for i in range(n) :
        print("$",end=' ')
        #print statement so that next lines are not concatinated
    print(end='\n')
    #to print the line with $ on the beginning and ending with space in between
    for i in range(n-2) :
        #printing the $ in the beginning
        print("$",end='')
        for j in range(((n+1)*2)-1) :
            #printing the extra spaces so that it can align
            print(" ",end='')
        #printing the last dollar
        print("$")
    for i in range(n) :
        print("$",end=' ')
    #printing the pattern if n = 1
elif n==1 :
    print('$')
    #telling the user that a pattern with the number they entered is not possible
