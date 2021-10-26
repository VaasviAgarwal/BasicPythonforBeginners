import csv
#defining function to create csv file
def createcsvfile():
    #creating a list which will later be converted to csv file
    records = [['Name', 'Total marks']]
    #seeing the number of students that the record will have
    n = int(input('Enter the number of students: '))
    print('The name name and total marks of the students one by one')
    #creating the nested list for n+1 rows with the first row being the heading
    for i in range(n):
        x=[]
        x.append(input('Enter the name of student: '))
        x.append(input('Enter the total marks of the student: '))
        records.append(x)
    #writing the data in the csv file
    with open('myfile.csv','w',newline='') as file:
        #creating an object for it
        csvobj=csv.writer(file, delimiter='\t')
        csvobj.writerows(records)
        print('myfile.csv is created with the student details')

#function that displays the details of the student from the csv files
def display():
    print('students read from myfile.csv')
    with open('myfile.csv','r',newline='') as file:
        #creating an object of the file to use
        csvobj = csv.reader(file, delimiter='\t')
        for row in csvobj:
            print(row)
        #printing plain line so next print is from a new line
        print()

#function to display the details of every third student
def display3():
    print('Details of every third student')
    with open('myfile.csv','r', newline='') as mainf:
        #converting the file back to a list to print the details of every third student
        l = list(csv.reader(mainf, delimiter='\t'))
        #i is the row number
        for i in range(len(l)):
            if i%3==0:
                print(l[i])

#main function
def main():
    createcsvfile()
    display()
    display3()

#driver code
if __name__ == '__main__':
    main()
    
        
