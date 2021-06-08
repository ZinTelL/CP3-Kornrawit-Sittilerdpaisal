number = int(input("Insert your how tall your christmas tree is?:"))
space = " "
for i in range(number):
   j = ((number-i)+2)
   print(((space*j)+"*"*(((i+1)*2)-1)))
