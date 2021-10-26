
#opening the file to be read
obj = open('demodata.txt','r+')
vl={'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
#reading the file
x = obj.read()

#printing the file to see if it has been read
print(x)
for i in x:
    if i=='a':
        vl['a']+=1
    if i=='e':
        vl['e']+=1
    if i=='i':
        vl['i']+=1
    if i=='o':
        vl['o']+=1
    if i=='u':
        vl['u']+=1
print('These are the count of the variables')
print(vl)
