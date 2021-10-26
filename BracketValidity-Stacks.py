s = input("Enter a string : ")
open = ['(', '{', '[']
close = [')','}',']']
stack = []
flag = 1
for i in s :
  if i in open :
    stack.append(i)
  elif i in close :
    c = close.index(i)
    if len(stack)==0:
      flag = 0
    elif stack[len(stack)-1]==open[c] :
      stack.pop()
    else :
      flag = 0
if flag == 0 :
  print('The brackets in the string entered are INVALID ')
elif len(stack)!=0:
  print('The brackets in the string entered are INVALID ')
else :
  print("The brackets in the string entered are VALID ")
