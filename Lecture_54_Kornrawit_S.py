def login():
    username = input("Username :")
    password = input("Password :")
    if username == "admin" and password == "Save":
        print("Login success")
        return True
    else:
        print("Login falied")
        return False

def showMenu():
    print("-------iShop-------")
    print("1. Vat calculator")
    print("2. Price calculator")

def menuSelect():
    userSelected = int(input(":"))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = totalPrice +(totalPrice*vat/100)
    return result

def priceCalculate():
    price1 = int(input("First Product Price :"))
    price2 = int(input("Second Product Price: "))
    return vatCalculate(price1+price2)

if login():
    showMenu()
    result = menuSelect()
    if result == 1:
        totalPrice = int(input("Your total price is:"))
        print(vatCalculate(totalPrice))
    elif result == 2:
        print("Price included vat:",priceCalculate(),"THB")