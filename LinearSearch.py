#assuming the user enters the correct datatype in all cases

#creating a function to make a list of size entered by the user
def createl():
    n = int(input('Enter the number of elements you want to be searched through'))
    print('Enter the elements')
    l = []
    #accepting the elements and creating a list which will be searched
    for i in range(n):
        l.append(input())
    #printing the list for clarity
    #returning the created list consisting of only string type datas
    return l

#function witht the linear search algorithm on the list passed, where the element will be accepted in it
#everything will be in the default datatype of string so there is no issue in comparison
def linearsearch(l):
    #accepting the element that need to be looked for
    s = input('Enter the character that you want to search')
    #for searaching we will have a for loop for the length of len(l) so that we can count when the element
    #was found
    #putting flag in case the element is not found
    f = 1
    for i in range(len(l)):
        if l[i]==s:
            print('The element found at index number:',i)
            #breaking so that if the element is found then it need not iterate again
            f = 0
            break
        print('The element not found at index number:',i)
    #if the value of i is equal to len(l) then the element was not present in the list
    if f :
        print('The element was not found')

#main function
def main():
    #calling the linear search with createl passed as argument so the list returned can be passed directly
    linearsearch(createl())

#driver code
if __name__=='__main__':
    main()






    
        
