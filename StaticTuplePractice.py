#performing the given functions on a static tuples

#function to create the tuple
def create1():
    return (1,2,5,7,9,2,4,6,8,10)

#to print halp of the values of the tuple in one line and other in next line
def displayhalf(t1):
    #finding length of the tuple and halving it (floor division as we need integer value)
    n = (len(t1))//2
    print('Answer to part (a) is:')
    #loop to print in first line till n(value at n will be excluded)
    for i in range(n):
        #ending with tab to seperte the values
        print(t1[i], end='\t')
    #printing a blank line after the loop so that next line prints on a new line
    print()
    #loop to print the second line from n to len(t1)
    for i in range(n,len(t1)):
        print(t1[i], end='\t')
    #printing a blank line after the loop so that the next line prints on a new line
    print()

#creating and printing a new tuple with even values of old tuple
def eventuple(t1):
    t = ()
    #appending the new tuple with even values of the old
    for i in t1:
        if i%2==0:
            t = t+(i,)
    #printing the new tuple
    print('The tuple with even elements of t1 is:')
    print(t)

#concatenating two tuples (both are static tuples
def con12(t1):
    #creating the second tuple
    t2 = (11, 13, 15)
    #concatinating them
    t1 = t1+t2
    #printing the answer
    print('The concatinated tuple is:')
    print(t1)

#finding and returning the maximnum and minimun values from the tuple
def maxmin(t1):
    #returning the values in a tuple so that it can returned at one
    return (max(t1), min(t1))

#main function
def main():
    #calling the functions in order
    #since the tuple is being returned it needs to be saved
    t1 = create1()
    #since the next 3 function are not returning anything they need not be saved
    displayhalf(t1)
    eventuple(t1)
    con12(t1)
    #since maximum and minimum values are being returned they need to be printed seperately
    #first store it in a variable
    mm = maxmin(t1)
    #maximun value is at index 0 and and minimun value is at index 1
    print('maximum value:',mm[0])
    print('minimum value:', mm[1])

#driver code
if __name__=='__main__':
    main()










