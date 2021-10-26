#assuming the user enters correct datatype
print('Enter the two numbers you want the lcm for : ')
a = int(input())
b = int(input())
def lcm(x, y) :
    if x<1 or y<1 :
        return 'The numbers you entered were invalid so no lcm could be calculated'
    else :
        ans = 1
        while True :
            if ans%x==0 and ans%y==0 :
                return ans
            ans=ans+1
print("The lcm of the numbers you entered is :")
print(lcm(a,b))
