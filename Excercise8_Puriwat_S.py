#Assignment
# 1 )Login (Username/PW)
# 2 Welcome+Product price shown ---> Choose Product
# 3 ) Input Product Q'ty-
#4 ) Summarize total price

print("DarkNEKO Product Order (V1.0)")
x=input("Please provide Username : ")
y=input("Please provide Password: ")
if x=='PuriwatS' and y=='21021994':
        print("Welcome to Product Catalogue Page ")
        print("Please select product as you needed")
        print("-----------------------------------")
        print("No.   Name                            Price (THB/Unit)    ")
        print("001     Shampoo (100 ml)                        40          ")
        print("002     Alcohol Hand Sanitizer (300 ml)          75         ")
        print("003     Instant Coffee  (40 pcs)                 150         ")
        print("004     Salmon Sasimi    (10 pcs)                200         ")
        print("-----------------------------------")
        print("Please input product  Q'ty needed for each Product")
        pd01=int(input(" No.001  :   "))
        pd02 = int(input(" No.002  : "))
        pd03 = int(input(" No.003  : "))
        pd04 = int(input(" No.004  :  "))
        print(" Total Price = ",(pd01*40)+(pd02*75)+(pd03*150)+(pd04*200),"THB")
else :
    print("Wrong Password , Please try again")






