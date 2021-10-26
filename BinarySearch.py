#Assuming the user enters the correct datatype in all cases

#function to create and return a list
def createl():
    #asking for the number of elements the user wants to enter assuming he enter a postive integer
    n = int(input('Enter the size of the list: '))
    #empty list
    l = []
    print('Enter the numeric values in an ascending order')
    #creating the list
    for i in range(n):
        l.append(int(input()))
    #returning the list
    return l

#checking if the user entered a sorted list and return true or false based on it
def checksort(l):
    #f that will be returned 1 if not sorted, 0 if sorted
    #initially we are assuming that the user entered a sorted list
    f = 0
    #if even 1 previous value is greater than the next value it will give false
    #excluding the last index from loop to avoid out of bound exception
    for i in range(len(l)-1):
        if l[i]>l[i+1]:
            f = 1
            break
    return f

def binarysearch(l):
    #accepting the element (keeping it as string)
    el = int(input('Enter the element to be searched: '))
    #putting low and high values initially as the very extremes of the values of the indexes
    low = 0
    high = len(l)-1
    #loop till high is greater than low
    while low <= high:
        #printing the flow
        print('Low is',low,'and High is',high)
        #calculating the middle index using floor so its a int value not float
        #high-low because it could be later as well
        mid = low +(high-low)//2
        if l[mid]==el:
            print('The element found at index number',mid)
            #ending the function here itself
            return
        #if element is greater than mid value, in the next iteration it will look in the second half
        elif l[mid]<el:
            low = mid+1
        #if element is less than mid value, in the next iteration it will look in the first half
        else :
            high = mid-1
    #if no value is returned even after the loop and the loop its looked through completely it means
    #element not in the list
    print('Element is not found in the list')

#main function
def main():
    #creating list and storing it
    l = createl()
    #checking if the list entered by the user is sorted
    #1 was returned if it was not sorted
    if checksort(l):
        print('The list entered by you is not sorted')
        #returning so next steps are not performed
        return
    #calling the binary search function
    binarysearch(l)

#calling main function
if __name__=="__main__":
    main()
    
        
        
        





















    
    #putting the initial low and high values of 
    
