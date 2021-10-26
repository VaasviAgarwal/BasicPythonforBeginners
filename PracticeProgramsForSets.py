#function to convert the strings passed in a string to sets
def conset(l):
    #x is the new list that will be passed which will have strings stored as sets
    x = []
    for i in l:
        x.append(set(i))
    return x

#function to indentify and display common characters stored in two different sets in a list
#using the intersection function for this purpose
def comm(l):
    #if there is no intersection then no value will be printed
    if (l[0]).isdisjoint(l[1]):
        print('There are no common values between the two')
        return
    x = (l[0]).intersection(l[1])
    print('The common characters in the sets of the given string are')
    for i in x:
        print(i, end=' ')
    print()
    return

#function to indentipy and display all distinct characters stored in two different sets in a list
def distinct(l):
    #using a function to find the symmetric difference between two sets
    x = (l[0]).symmetric_difference(l[1])
    #printing the elements of u now that it does not have intersecting elements
    if len(x)==0:
        print('There are no distinct characters in them')
        return
    print('The distince elements in the sets of the given string are')
    for i in x:
        print(i, end=' ')
    print()
    return

#main function
def main():
    #accepting two strings and appending them to an empty list l
    l = []
    print('Enter two strings')
    l.append(input())
    l.append(input())
    #converting the elements of the list
    l = conset(l)
    #printing the common characters of the two
    comm(l)
    #printing the distinct characters of the two
    distinct(l)

if __name__=='__main__':
    main()






    
