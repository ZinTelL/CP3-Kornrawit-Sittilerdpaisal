BasketballBalls = 350
SoccerBalls = 400
TennisBalls3x = 300
GymnasticBalls = 700
VolleyBalls = 200

userName = input("Enter your username please : ")
passCode = input("Enter your passcode please : ")
if userName == "Save" and passCode == "Kornrawit":
    print("Welcome!, These are our available products.")
    print("Enjoy your shopping days and take your time")
    print("1.)Basketball balls",BasketballBalls,"THB")
    print("2.)Soccer balls",SoccerBalls,"THB")
    print("3.)Tennis balls 3x pack",TennisBalls3x,"THB")
    print("4.)Gymnastic balls",GymnasticBalls,"THB")
    print("5.)Volleyball balls",VolleyBalls,"THB")
    productNumber = int(input("Please enter number of your product :"))
    if productNumber == 1:
        quantity = int(input("How much do you want :"))
        print("Summary price is :",quantity,"x",BasketballBalls,quantity*BasketballBalls,"THB")
        print("Thank you for visiting us, please come back again")
    elif productNumber == 2:
        quantity = int(input("How much do you want :"))
        print("Summary price is :", quantity, "x",SoccerBalls, quantity * SoccerBalls, "THB")
        print("Thank you for visiting us, please come back again")
    elif productNumber == 3:
        quantity = int(input("How much do you want :"))
        print("Summary price is :", quantity, "x",TennisBalls3x, quantity * TennisBalls3x, "THB")
        print("Thank you for visiting us, please come back again")
    elif productNumber == 4:
        quantity = int(input("How much do you want :"))
        print("Summary price is :", quantity, "x", GymnasticBalls, quantity * GymnasticBalls, "THB")
        print("Thank you for visiting us, please come back again")
    elif productNumber == 5:
        quantity = int(input("How much do you want :"))
        print("Summary price is :", quantity, "x",VolleyBalls, quantity * VolleyBalls, "THB")
        print("Thank you for visiting us, please come back again")
else:
    print("Wrong username or passcode")
