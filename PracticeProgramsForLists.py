#inputing a list and converting it from string to list
def inputlist():
    #accepting input in the form of a list
    #assuming that the user follows the rules for entering a string as mentioned in the print statements
    print('Enter a list ',end='')
    print( '(if entering a string enclose the element in '' and enclose all the elements in [] seperated by ", ") :')
    l = eval(input())
    return l

#function that checks if the datatype of the whole list is same as the one it is called with
def typecheck(l, datatype):
    #l is the list passed by the user
    #datatype is the type that needs to be checked for
    #checking if the given list is of elements of the given datatype by using a counter variable f
    #returning the f afteer the loop
    #f is initially true and remain true if its the same datatype throughout the list
    f=1
    for i in l:
        if type(i) != datatype :
            f=0
    return f

#counting the number of odd elements in the list
def countodd(l):
    #l is the numerical list passed
    #c stores the count and will be returned later
    c=0
    for i in l:
        if i%2 != 0 :
            c=c+1
    return c

#counting the number of numeric strings in the list
def countnum(l):
    #l is the string list passed
    #c stores the number of numeric strings
    c=0
    for i in l:
        if i.isnumeric():
            c=c+1
    return c

#counting the number of alphabetical string in the list
def countalpha(l):
    #l is the string list passed
    #c stores the number of alphabetical strings
    c=0
    for i in l:
        if i.isalpha():
            c=c+1
    return c

#main function
def main():
    l=inputlist()
    #checking if its a numerical string
    if typecheck(l,int):
        print('The list is a numerical list')
        #if numeric string then we have to count the number of odd elements in the string
        print('The number of odd number elements in the list are', countodd(l))
    #if not numeric then we have to check if its a list only with strings
    elif typecheck(l,str):
        print('The list only has strings')
        #if all are strings then we have to check for the largest string in it
        print('The largest string in the list by ASCII value is :',  max(l))
        #for the length wise out of two equal lenght of  strings it will choose the first one
        print('The largest string in the list by length is :', max(l,key=len))
        #if string then when need to count the number of alpha and num elements
        print('There are',countalpha(l),'alphabetical strings in the list')
        print('There are',countnum(l),'numeric strings in the list')
    else:
        #All the elements in the list are not of the same datatype
        print('The list is neither completely numerical nor string')

        
#drivercode
if __name__=="__main__":
    main()
    
        
