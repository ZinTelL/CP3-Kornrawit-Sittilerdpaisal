menuList = []
priceList = []

def showBill():
    totalPrice = 0
    print("----My Food ----")
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice = totalPrice+int(priceList[number])
    print("Total price :",totalPrice,"THB")



while True:
    menuName = input("Please Enter Menu: ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price (THB) :")
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()