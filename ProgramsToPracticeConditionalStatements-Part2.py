#assignment7 practicing conditional statements
#assuming the user will enter the correct datatype everytime asked for an input
print("Following is the menu of functions that can be performed")
print("6 to input week number and print week day.")
print("7 to check whether a character is alphabet or not")
print("8 to input any alphabet and check whether it is vowel or consonant")
print("9 to input any character and check whether it is alphabet, digit or special character")
print("10 to check whether a character is uppercase or lowercase alphabet")
print("11 to  tell the customer how much discount they will get on their total amount")
choice = int(input("Enter your choice : "))
#to print the weekday corresponding to the number
#sunday == 1 and saturday == 7
if choice == 6 :
    day = int(input("Enter a number between 1 and 7 : "))
    if day == 1 :
        print("The day corresponding to the number entered by you is Sunday")
    elif day == 2 :
        print("The day corresponding  to the number entered by you is Monday")
    elif day == 3 :
        print("The day corresponding to the number entered by you is Tuesday")
    elif day == 4 :
        print("The day corresponding to the number entered by you is Wednesday")
    elif day == 5 :
        print("The day corresponding to the number entered by you is Thursday")
    elif day == 6 :
        print("The day corresponding to the number entered by you is Friday")
    elif day == 7 :
        print("The day corresponding to the number entered by you is Saturday")
    else :
        print("The number you entered was out of range")

#to check if the character entered by the user is an alphabet or not
elif choice == 7 :
    char = input("Enter a character : ")
    #code is to store the ASCII value of the character
    code = ord(char)
    if (code >= 65 and code <= 90) or (code >= 97 and code <= 122) :
        print("The character entered by you is an alphabet")
    else :
        print("The character entered by you is not an alphabet")

#to  check if the character entered by the user is a vowel or a consonant
elif choice == 8 :
    char = input("Enter an alphabet : ")
    #code is to store the ASCII value of the alphabet entered by the user
    code = ord(char)
    if code == 65 or code == 69 or code == 73 or code == 79 or code == 85 :
        print("The character entered by you is a vowel")
    elif code == 97 or code == 101 or code == 105 or code == 111 or code == 117 :
        print("The character entered by you is a vowel")
    elif code < 65 or (code>90 and code<97) or code>122 :
        print("Invalid input : The character entered by you is not an alphabet")
    else :
        print("The character entered by you is a consonant")

#to check whether the character entered is an alphabet, a number or a special character
elif choice == 9 :
    char = input("Enter a character : ")
    #code is to store the ASCII value of the character entered by the user
    code = ord(char)
    if (code >= 65 and code <= 90) or (code >= 97 and code <= 122) :
        print("The character entered by you is an alphabet")
    elif code >= 48 and code <= 57 :
        print("The character entered by you is a number")
    else :
        print("The character entered by you is a special character")

#to check whehter the alphabet entered by the user is in lowercase or uppercase 
elif choice == 10 :
    char = input("Enter an alphabet : ")
    #code is to store the ASCII value of the character entered by the user
    code = ord(char)
    if code >= 65 and code <= 90 :
        print("The alphabet entered by you is in UpperCase")
    elif code >= 97 and code <= 122 :
        print("The alphabet entered by you is in LowerCase")
    else :
        print("Invalid input : The character by you is not an alphabet")

#to check the amount of discount the user will get based on the total amount entered by them
#below 500 no discount, from 500 to 1000 5% discount and 1000 and above will get 10% off
elif choice == 11 :
    total_amount = float(input("Enter the total amount for your purchase : "))
    if total_amount < 0 :
        print("Invalid Input : The value entered by you is negative")
    elif total_amount < 500 :
        print("You will get no discount, your final amount will be",total_amount)
    elif total_amount < 1000 :
        print("You will get 5% off, your final amount will be",(total_amount-(total_amount*0.05)))
    else :
        print("You will get 10% off, your final amount will be",(total_amount-(total_amount*0.1)))

#to check if the user enters the wrong choice 
else :
    print("Invalid input : The number entered by you was not present in the choice")
#end of program
