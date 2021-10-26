#print the table of a number till for limit number entered by the user
#accepting the number for which the table has to be printed assuming they will enter a postive number
n = int(input("Enter a positive number till which you want the table to be printed : "))
#accepting the limit till where the user wants the table assuming user will enter a positive number
limit = int(input("Enter the largest number till where you want the table : "))
#declaring and initializing i as the variable which will keep track of the table
i=1
#while loop till the tracking number is less than or equal to the limit provided by the user
while (i < (limit+1)) :
    #printing the table
    print(i,"x",n,"=",(i*n))
    #increment in i so that the table for the next number can be printed in the next run of the loop
    i=i+1
#program ended
