#โจทย์เดิมจาก Lecture ที่ 71
# Assignment: หาราคารวมของสินค้าทั้งหมด แต่ปรับใหม่ให้คิดราคารวมจาก list of list
menuList=[]

def ShowBill():
    sumPrice = 0
    print("YummiNinja".center(25,"*"))
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        sumPrice+=int((menuList[number][1]))
    print("Total Price is ",sumPrice,"THB")

while True:
    menuName=input("Please enter Menu : ")
    if (menuName.lower() =="exit"):
        break
    else:
        menuPrice=input("Price : ")
        menuList.append([menuName,menuPrice]) # added menuPrice
        #PriceList.append(menuPrice) #Disbled PriceList
ShowBill()






