#assuming that the user enters values of correct datatypes
n = int(input("Enter  the number of terms you want in the fibonacci series : "))
#giving the output without recursion
print("The result without recursion is")
if n < 1 :
    print("Invalid entry")
elif n == 1 :
    print('0')
elif n == 2 :
    print('0, 1',end='')
else :
    a = 0
    b = 1
    print('0, 1',end='')
    for i in range(2,n) :
        c = a+b
        print(', ',c,end='')
        a = b
        b = c
print()
#generationg fibonnaci series with recursion
print("The result with recursion is")
def fib(a,b,c,m) :
    if m<1 :
        print("Invalid entry")
        return 
    if c>=m :
        return
    print(a,end=',  ')
    b = a+b
    a = b-a
    return fib(a,b,c+1,m)
fib(0,1,0,n)


