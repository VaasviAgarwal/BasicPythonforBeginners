
#importing math module
import math
#function to find the angle in radians
def angle(n):
    return (n/180)*(22/7)

#funciton to print the angle in terms of pi
def angdis(x):
    #for 0, 180 and 360 degreees
    if x%180==0:
        print('(',x//180,')pi', sep='',end='\t')
    #for 90 and 270 degrees
    elif x%90==0:
        print('(',x//90,'/2)pi', sep='', end='\t')
    #for 45, 135, 225 and 315 degrees
    else:
        print('(',x//45,'/4)pi', sep='', end='\t')

#function that prints the value of sin, cos tan of the angle for 1 decimal value
#n is the angle in radians for which we need answer
def anstab(n):
    print(round(math.sin(n), 1), round(math.cos(n), 1), round(math.tan(n), 1), sep='\t')

#main function
def main():
    #x here ranges from 0 to 360 on intervals of 45 and is in radians
    #using tab to seperate them so its distinct
    #first line is printing the headings
    print('angle x', 'sin(x)', 'cos(x)', 'tan(x)', sep='\t')
    #using for loop to traverse
    #using x instead of i as loop variable. step is 45 and ends at 361(not included)
    #angle is rounded of angle to 1 decimal place
    for x in range(0,361,45):
        a = angle(x)
        angdis(x)
        anstab(a)

#driver code
if __name__=="__main__":
    main()



    ggg
