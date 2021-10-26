#assuming that the user enters correct datatype in all cases

#function to find the position entered by the user
#will give the answer as the position and not the index number
def pos():
    s = input("Enter the string in which substring wil be looked for : ")
    a = input("Enter the substring we are looking for : ")
    x = 1+s.find(a)
    if x == 0 :
        print("The substring entered by you is not present")
        return
    print("The substring is present at postition(not the index number) is",x)
    return

#function to replace good with best in the given string
#if good is not present in the string given then a message will be displayed
def rep():
    s = input("Enter the string which you wish to be updated : ")
    if s.find('good')==-1 :
        print("The string that you entered does not have 'good' in it")
        return
    print("The updated string is :")
    print(s.replace('good','best'))
    return

#function to split the string into parts with botht split and partition functions
#if will inform the user if the substring entered by them is not a part of the string
def seperate():
    a = input("Enter the string that needs to be split : ")
    b = input("Enter the delimited part or the string from which it has to be seperated : ")
    if a.find(b)==-1:
        print("The delimited part is not present in the string")
        return
    x = a.split(b)
    y = a.partition(b)
    print("The answer through split function is :",x)
    print("The answer through partition function is :",y)
    return

#function that accepts a string and prints its titilized version
def contit():
    s = input("Enter the text you want to be converted into title form : ")
    print("The title form of the text entered by you is :")
    print(s.title())
    return

#function to accept and swap the cases of a string
def loupp():
    s = input("Enter the string in which you want the cases to be swaped : ")
    print("The answer with swapped cases is :")
    print(s.swapcase())
    return

#a function to tell the user that he has entered an invalid value as a choice
def invalid():
    print("Invalid entry")
    return

#a function that prints the menu everytime is is called and then returns the choice
def menu11():
    print("Enter the number next to operation you wish to perform")
    print("1 to look for a substring in the given string and returns its position.")
    print("2 to replace substring 'good' with 'best' in the given string.")
    print("3 to find all the substring in the string which are separated by delimited.")
    print("4 to convert the given text into title form.")
    print("5 to convert lowercase to uppercase and uppercase to lowercase in the given string.")
    print("6 to Exit")
    return int(input("Enter your choice : "))

#main function where everything is happening
def main():
    while True :
        choice = menu11()
        if choice == 1 :
            pos()
        elif choice == 2 :
            rep()
        elif choice == 3 :
            seperate()
        elif choice == 4 :
            contit()
        elif choice == 5 :
            loupp()
        elif choice == 6 :
            #if the user entere 6 then the main function will be terminated with a statement telling why
            print("The program has been terminated/exited as you entered 6")
            return
        else :
            invalid()
        #printing a line of characters so that everytime the loop is being run again can be distinguished
        print("**********************************************************************")

#driver code
if __name__ == "__main__" :
    main()



    
