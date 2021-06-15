menuList = []
def showBill():
    totalPrice = 0
    print("----My Food ----")
    for number in range(len(menuList)):
        totalPrice = totalPrice+int(menuList[number][1])
        print(menuList[number][0])
    print("Total price:",totalPrice,"THB")

while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price (THB) :")
        menuList.append([menuName,menuPrice])
print(menuList)
showBill()