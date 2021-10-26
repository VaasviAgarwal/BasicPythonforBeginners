
#assuming the user enters correct datatype in all cases
print("Enter 1 if you want to calculate the area of a square")
print("Enter 2 if you want to calculate the area of a rectangle")
print("Enter 3 if you want to calculate the area of a circle")
print("Enter 4 if you want to calculate the area of a triangle")
choice = int(input("Enter your choice : "))

#calculating area of a square
if choice == 1 :
    #defining a function for area of square
    def area_of_square() :
        side = float(input("Enter the length of the square : "))
        #asserting that the user does not enter a negative value as the length
        assert side>=0 , 'length entered is less than zero'
        #returning the area of square
        return (side*side)
    #calling and printing the answer
    print(area_of_square())

#calculating area of a rectangle
elif choice == 2 :
    #defining a function for area of rectangle
    def area_of_rectangle() :
        length = float(input("Enter the length of the rectangle : "))
        breadth = float(input("Enter the breadth of the rectangle : "))
        #asserting that the user does not enter a negative value as the length and breadth
        assert length>=0 and breadth>=0  , 'value entered as sides is less than zero'
        #returning the area of rectangle
        return (length*breadth)
    #calling and printing the answer
    print(area_of_rectangle())

elif choice == 3 :
    #defining a function for area of circle
    def area_of_circle() :
        radius = float(input("Enter the radius of the circle : "))
        #asserting that the user does not enter a negative value as the radius
        assert radius>=0 , 'radius entered is less than zero'
        #returning the area circle
        return (radius*radius*(22/7))
    #calling and printing the answer
    print(area_of_circle())

#calculating area of a rectangle
elif choice == 4 :
    #defining a function for area of triangle
    def area_of_triangle() :
        height = float(input("Enter the height of the triangle : "))
        base = float(input("Enter the length of base of the triangle : "))
        #asserting that the user does not enter a negative value as the height and base
        assert height>=0 and base>=0  , 'value entered as sides is less than zero'
        #returning the area of triangle
        return (height*base*0.5)
    #calling and printing the answer
    print(area_of_triangle())

#checking if the user entered anything other than the required value as the choice
else :
    print("Invalid value entered as a choice")






    

