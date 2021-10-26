#program to accept number of seconds from the user and represent it in terms of days, hours, minutes and seconds
#accepting number of seconds n from the user and assuming that the user enters a positive integer value as an input and save the same value in a for the end
n=int(input("Enter the number of seconds : "))
a=n
#seconds left at the end of calculation will be n%60
sec=n%60
#now remove extra seconds and convert n to minutes by dividing it by 60
n=n//60
#now minutes left at the end will be n%60
minutes=n%60
#now convert the rest of the n minutes to hours by diving it by 60
n=n//60
#hours left at the end of calculation will be n%24
hours=n%24
#now convert rest of the n hours left to days by diving it with 24
days=n//24
print(a,"seconds will be",days,"days,",hours,"hours,",minutes,"minutes and",sec,"seconds")
