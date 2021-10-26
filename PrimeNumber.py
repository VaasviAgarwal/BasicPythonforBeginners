#assuming that the user enters the correct datatype in all cases
#function returns True if the number is prime else it returns true
def prime(m) :
    if m == 1 :
        return False
    else :
        a = 2
        c = 0
        while a <= m :
            if (m%a)==0 :
                c = c+1
            a = a+1
        if c == 1 :
            return True
        else :
            return False

#writing the part where we accept a number from the user to print all prime number till that number
n = int(input("Enter a natural number : "))
if n < 1 :
    print("The number you entered is not a natural number")
else :
    print("The list of all prime numbers till",n,"are :")
    for i in range(1,n+1) :
        if prime(i) :
            print(i)




