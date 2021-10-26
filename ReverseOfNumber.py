#assuming the user enters correct datatype of the numbers
def my_fun(n) :
    if n<0 :
        a = n-(2*n)
    else :
        a = n
    r = 0
    s = 0
    while a > 0 :
        r = (r*10) + (a%10)
        s = s + (a%10)
        a = a//10
    if n < 0 :
        r = -r
    print("reverse of the number is",r)
    print("sum of the digits of the number is",s)

#calling the function
my_fun(int(input("Enter an integer number : ")))

