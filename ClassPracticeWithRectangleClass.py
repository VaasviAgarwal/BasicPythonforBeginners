#assuming that the user enters the correct datatype in all cases

#creating a class rectangle
class Rectangle:
    #constructor for initializing the values
    def __init__(self, l, b):
        #initializing values
        self.length=l
        self.breadth=b

    #deconstructor
    def __del__(self):
        print('The destructor is called')

    #function to calculate and return the area
    #since values have already been initialized in constructor we do not need to pass them in arguments
    def area(self):
        return self.length * self.breadth

    #function to calculate and return the perimeter of the area
    #no arguments for the same reason as area function
    def perimeter(self):
        return 2 * (self.length + self.breadth)

#main function
def main():
    #accepting the values of length and breadth
    #assuming the user enters a postive integer value
    x = int(input('Enter the length of the rectangle: '))
    y = int(input('Enter the breadth of the rectangle: '))
    #creating an object of the class Rectangle with x, y as its parameters
    ob = Rectangle(x,y)
    #Calling the area  and rectangle functions with the object and printing them in directly so they need
    #not be saved
    print('Area of the rectangle is', ob.area())
    print('Perimeter of the rectangle is', ob.perimeter())
    #calling the deconstructor/destructor
    del ob

#calling main function
if __name__=='__main__':
    main()










    
