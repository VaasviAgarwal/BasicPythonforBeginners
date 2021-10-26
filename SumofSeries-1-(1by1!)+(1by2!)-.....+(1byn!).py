#assuming the user enters the correct datatype in all cases
#1-1/1! + 1/2! - 1/3! + ..... + 1/n is the series whose sum we need to find

#recursive function for calculating the factorial of a number
#the factorial will be calculated be multiplying the numbers backwards unlike that in for loop
def fact(n):
    if n==1:
        return 1
    return fact(n-1)*n

#function to see if the factorial should be postive or negative
#the function returns 1 if the number passed is even and -1 if the number passes is positive
#the value returned by the function can be multiplied in the value that will be added to the series
def pn(n) :
    if n%2==0 :
        return 1
    return -1

#main function
def main():
    #accepting the value of n from the user
    n = int(input("Enter the n value of n which is greater than or equal to 0 : "))
    #if the user has entered a value less than n then there will be a message displayed explaining
    #return statement will bring us out of the main function so that no further code will be run
    if n<0 :
        print("Invalid value of n entered")
        return
    #sum is equal to 1 initially so that the loop only needs to calculate the factorials starting from 1
    #and if the value of n = 0 then the answer will be 1
    s = 1
    #loop starts from 1 as we do not need to calculate the factorial for 0th term
    for i in range(1,n+1):
        s = s + ( ( 1 * pn(i) ) / fact(i) )
    print('Answer =',s)

#drinver code
if __name__== "__main__" :
        main()






    
