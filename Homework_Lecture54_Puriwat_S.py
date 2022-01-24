vat = 7
def login():
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
    if usernameInput == "admin" and passwordInput == "1234":
        return showMenu()
    else:
        print("Please Try Again")
        return login()

def showMenu():
    print("----- iShop -----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuSelect()

def menuSelect() :
    print("Please select your menu (type 1 or 2) ")
    userSel = input(">>")
    if userSel == "1":
        return vatCalculator()
    elif userSel == "2":
        return priceCalculator()
    else:
        return showMenu()


def vatCalculator () :
    print("Please specify your product price")
    totalPrice=float(input("Product price : "))
    return print("Total price will be ",totalPrice + (totalPrice * vat / 100), "THB")

def priceCalculator():
    print("Please specify your product price")
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    totalPrice2=price1+price2
    return print("Total price will be ",totalPrice2 + (totalPrice2 * vat / 100), "THB")

(login())
