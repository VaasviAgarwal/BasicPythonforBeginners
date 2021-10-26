#assuming the user enters the correct datatype in all cases

#class student with functions and class variables that will be called
class student:
    #initializing the maximum average marks, maxam at 0
    maxam=0
    #initializing the values
    def __init__(self, name, roll, hindi, english, maths):
        #using the self keyword to initialize and the values
        self.name=name
        self.roll=roll
        #creating a dictionary to store marks
        self.marks=dict([('Hindi',hindi), ('English',english), ('Maths', maths)])

    #function to display the values member wise
    def disbmem(self):
        print(self.name, self.roll, self.marks['Hindi'], self.marks['English'],  self.marks['Maths'], sep='\t', end='\t')
        #calculating average marks by dividing the sum of all values of marks by its len
        self.am = sum(self.marks.values())/len(self.marks.values())
        #printing the average marks
        print(self.am)
        #updating the value of maximum average marks if it is less than the average marks we just saw
        if type(self).maxam<self.am:
            type(self).maxam=self.am
#class ends

#function to display the maximum average marks (function out side the class)
def dismax():
    print('Maximum average marks out of all the students:', student.maxam)

#defining main function
def main():
    n=int(input('Enter number of students: '))
    #creating empty list to pass
    l = []
    #for loop from 1 to n+1 as n+1 will be excluded
    for i in range(1,n+1):
        #accepting the details of the student
        name = input('Enter name of the Student%s: '%i)
        roll = int(input('Enter roll number of the Student%s: '%i))
        hindi = int(input('Enter the Hindi of the Student%s: '%i))
        english = int(input('Enter the English of the Student%s: '%i))
        maths = int(input('Enter the Maths of the Student%s: '%i))
        #creating the the object for that student and appending it in list
        l.append(student(name,roll,hindi,english,maths))
    #printing the first line for the table
    print('Name','Roll No.', ' Hindi', 'English', 'Maths', 'Average', sep='\t')
    #for loop in l for displaying the details of each student through the method of class
    for i in l:
        i.disbmem()
    #displaying the maximum average marks
    dismax()

#calling main fuction
if __name__=='__main__':
    main()

        
        






    
