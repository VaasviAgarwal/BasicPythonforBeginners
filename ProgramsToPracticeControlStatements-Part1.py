#menu driven program for practicing control statement
#assuming that the user enters the correct data type in all cases
#i will be the loop variable in most cases
#a loop will run till the time user does not want to terminate the program by chosing the correct option
print("Enter 1 if you want all natural numbers from 1 to n be printed")
print("Enter 2 if you want multiplication table of any number till where you want to be printed")
print("Enter 3 if you want all natural numbers in reverse (from n to 1) to be printed")
print("Enter 4 if you want all even numbers between 1 to 100 to be printed including 1 and 100")
print("Enter 5 if you want all odd number between 1 to 100 to be printed  including 1 and 100")
print("Enter 6 if you want to find sum of all natural numbers between 1 to n and print it")
print("Enter 7 if you want to find sum of all even numbers between 1 to n and print it")
print("Enter 8 if you want to find sum of all odd numbers between 1 to n and print it")
print("Enter 9 if you want to count number of digits in a number entered by you and print it")
print("Enter 0 if you want to terminate the loop")
choice = int(input("Enter your choice : "))
while choice != 0 :

    #to print all natural numbers from 1 to n where n is entered by the user
    if choice == 1 :
        n = int(input("Enter the value of n : "))
        if n<1 :
            print("Invalid entry : Natural numbers are greater than 0 and number entered by you was not")
        else :
            i = 1;
            print("The natural numbers are :")
            while i <= n :
                print(i)
                i = i + 1

    #to print the muliplication table of a number and printing it till the number you want
    elif choice == 2 :
        n = int(input('Enter the number you want the table for : '))
        limit = int(input('Enter the largest number you want the table/ multiplication for : '))
        i = 1
        print("The table of",n,"is as follows :") 
        while i <= limit :
            print(n,'x',i,'=',(n*i))
            i = i + 1

    #to print all the natural numbers in reverse ie from n to 1
    elif choice == 3 :
        n = int(input("Enter the value of n : "))
        if n < 1 :
            print("Invalid entry : Natural numbers start from 1 and you entered a value smaller than that")
        else :
            print("The natural numbers in reverse order are :")
            i = n
            while i >= 1 :
                print (i)
                i = i - 1

    #to print all even numbers between 1 and 100 including 1 and 100
    elif choice == 4 :
        i = 2
        print("All even numbers between 1 and 100 including 1 and 100 are :")
        while i <= 100 :
            print(i)
            i = i + 2

    #to print all odd numbers between 1 and 100 including 1 and 100
    elif choice == 5 :
        i = 1
        print("All odd numbers between 1 and 100 including 1 and 100 are :")
        while i <= 100 :
            print(i)
            i = i + 2

    #to print the sum of natural numbers between 1 and n
    elif choice == 6 :
        n = int(input("Enter the value of n : "))
        if n < 1 :
            print('Invalid entry : Natural numbers start from 1 and your entry is smaller than that')
        else :
            i = 1
            #s is the variable used to store the value of sum
            s = 0
            while i <= n :
                s = s + i
                i = i + 1
            print('The sum of all natural numbers from 1 to',n,'is',s)

    #to print the sum of all even numbers from 1 to n
    elif choice == 7 :
        n = int(input('Enter the value of n : '))
        s = 0
        if n < 1 :
            i = 0
            while i >= n :
                s = s + i
                i = i - 2
        else :
            i = 2
            while i <= n :
                s = s + i
                i = i + 2
        print("The sum of all even numbers from 1 to",n,'is',s)

    #to print the sum of all odd numbers from 1 to n
    elif choice == 8 :
        n = int(input('Enter the value of n : '))
        s = 0
        i = 1
        if n < 1 :
            while i >= n :
                s = s + i
                i = i - 2
        else :
            while i <= n :
                s = s + i
                i = i + 2
        print("The sum of all odd numbers from 1 to",n,'is',s)

    #to count the number of digits in the number entered by the user
    elif choice == 9 :
        n = int(input('Enter a number : '))
        if n != 0 :
            if n < 0 :
                a = n - (n*2)
            else :
                a = n
            count = 0
            while a>0 :
                count = count + 1
                a = a // 10
            print(n,'has',count,'digits')
        else :
            print("0 has 1 digits")
    
    #telling the user that the choice they entered is not available
    else :
        print("Inavlid entry : The choice you made was not available")

    #printing symbols so a disctinction can be made each time user enters a choice
    print("------------------------------------------------------------------------------------------------------------------------")

    #giving the menu and option to choose again
    print("Enter 1 if you want all natural numbers from 1 to n be printed")
    print("Enter 2 if you want multiplication table of any number till where you want to be printed")
    print("Enter 3 if you want all natural numbers in reverse (from n to 1) to be printed")
    print("Enter 4 if you want all even numbers between 1 to 100 to be printed including 1 and 100")
    print("Enter 5 if you want all odd number between 1 to 100 to be printed  including 1 and 100")
    print("Enter 6 if you want to find sum of all natural numbers between 1 to n and print it")
    print("Enter 7 if you want to find sum of all even numbers between 1 to n and print it")
    print("Enter 8 if you want to find sum of all odd numbers between 1 to n and print it")
    print("Enter 9 if you want to count number of digits in a number entered by you and print it")
    print("Enter 0 if you want to terminate the loop")
    choice = int(input("Enter your choice : "))

#if choice is equal to zero then the loop and program will be terminated
print("The program has been terminated as you chose 0")
