#function that perform the task of printing a dictionary where the keys are values from 1-5 and values are their cubes
def cubed():
    #declaring an empty dictionary
    d = {}
    #creating a for loop where i goes from 1 to 5
    for i in range(1,6): #6 as last value is exculeded
        d.update({i:(i**3)}) #updating or adding a key value pair to the dictionary each time
    #printing the final dictionary
    print('The dictinary having number from 1  to 5 as the keys and their cubes as their values :')
    print(d)

#main function
def main():
    #calling the function that does the required task
    cubed()

#driver code
if __name__=='__main__':
    main()
