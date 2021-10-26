#assuming the user enters the data in the correct datatype and following the requirements
#sorting the values according to their ASCII values as making a list of string element only

#function to create a list
def createl():
    #accepting the size of the array. Assuming the user enters a positive integer
    n = int(input('Enter the size of the list: '))
    print('Enter the elements')
    #creating an empty list initially
    l = []
    #creating the list
    for i in range(n):
        l.append(input())
    print('Unsorted list as entered by you:',l)
    #returning the list
    return l

#creating a selection sort function on the list passed as the argument
def selectionSort(l):
    #first function in range len(l) so last index is len(l)-1 is excluded to avoid error
    for i in range(len(l)):
        #assuming that the value at i is initially less than all the values after it in the list so putting that as
        #the min index
        m = i
        #running a loop on all the values in the list after the one at the current index
        for j in range(i+1, len(l)) :
            #since we are sorting in ascending order we are checking for values less than l[m] and updating m
            #if we were sorting in descending order we would look for values greater than l[m] to update m
            if l[j]<l[m]:
                #if l[j] is less than l[m] then we will update m. That means m will be the index at which the
                #minimum values in the sublist from i to len(l) is stored
                m = j
            #once the whole loop is traversed we will exchange value at l[i] and l[m]
        l[i], l[m] = l[m], l[i]
        print('Pass -->',i+1,l)
    #printing the sorted list
    print('Sorted list in ascending order according the ASCII values is:',l, sep='\n')

#defining main function
def main():
    #calling createl for creating  and storing a list l
    l = createl()
    #calling the sorting funciton
    selectionSort(l)

#calling the main function
if __name__ =='__main__':
    main()







    




    
    





            
        
