#  โจทย์เดิมจาก Lecture ที่ 72
# Assignment1 : ปรับแก้เป็นให้ user หาราคาสินค้าจาก list สินค้าที่มีอยู่แล้ว
#  หลังจากนั้นหาราคารวม
menuList=[]
Original_info={"ข้าวมันไก่":60,"ข้าวหมูทอด":75,"ข้าวขาหมู":80}

while True:
    menuName=input("Please enter Menu : ")
    if (menuName.lower() =="exit"):
        break
    else:
        menuList.append([menuName,Original_info[menuName]])


def ShowBill():
    sumPrice = 0
    print("YummiNinja".center(25, "*"))
    for number in range(len(menuList)):
        print(menuList[number][0], menuList[number][1])
        sumPrice += int((menuList[number][1]))
    print("******************************")
    print("Total Price is ", sumPrice, "THB")

print(menuList)
ShowBill()

