#program to find the number of times each vowel occurs in a string
#function to check if the character passed is a
def ifa(x):
    if x == 'a' or x =='A' :
        return 1
    return 0
#function to check if the character passed is e
def ife(x):
    if x == 'e' or x=='E' :
        return 1
    return 0
#function to check if the character passed is i
def ifi(x):
    if x == 'i' or x=='I' :
        return 1
    return 0
#function to check if the character passed is o
def ifo(x):
    if x == 'o' or x=='O' :
        return 1
    return 0
#function to check if the character passed is u
def ifu(x):
    if x == 'u' or x=='U' :
        return 1
    return 0

#main function
def main():
    s = input('Enter a string: ')
    #variables to count each of them assigned to 0
    ac = 0
    ec = 0
    ic = 0
    uc =0
    oc= 0
    #loop to go through each character
    for i in s :
        #if the current character is a vowel its function will return 1
        #and its count will be incremented
        #rest all will be incremented by 0
        ac = ac + ifa(i)
        ec = ec + ife(i)
        ic = ic + ifi(i)
        oc = oc + ifo(i)
        uc = uc + ifu(i)
    #printing the answer
    print('The following is the number of times each vowel is present')
    print('a =',ac)
    print('e =',ec)
    print('i =',ic)
    print('o =',oc)
    print('u =',uc)

#driver code
if __name__ =="__main__" :
    main()
