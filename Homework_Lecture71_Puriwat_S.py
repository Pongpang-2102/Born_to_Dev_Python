#โจทย์เดิมจาก Lecture ที่ 71
# Assignment: หาราคารวมของสินค้าทั้งหมด
menuList=[]
PriceList=[]

def ShowBill():
    sumPrice = 0
    print("YummiNinja".center(25,"*"))
    for number in range(len(menuList)):
        print(menuList[number],PriceList[number])
        sumPrice+=int(PriceList[number])
    print("Total Price is ",sumPrice,"THB")

while True:
    menuName=input("Please enter Menu : ")
    if (menuName.lower() =="exit"):
        break
    else:
        menuPrice=input("Price : ")
        menuList.append(menuName)
        PriceList.append(menuPrice)
ShowBill()





