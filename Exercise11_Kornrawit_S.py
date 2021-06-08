line = int(input("Insert your how tall your christmas tree is?:"))
spaceCharacter = " "
starCharacter = "*"
for i in range(line):
   totalSpace = line-(i+1)
   totalStar = (((i+1)*2)-1)

   space = totalSpace * spaceCharacter
   star = totalStar * starCharacter

   print(space+star)


print("Merry christmas")
