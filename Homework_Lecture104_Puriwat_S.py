class Customer:
    name=""
    lastName=""
    age=0
    def addCart(self):
        print("Added Product to ",self.name,self.lastName,"'s cart")

customer1=Customer()
customer1.name="Puriwat"
customer1.lastName="Sangrawee"
customer1.age=27
customer1.addCart()

customer2=Customer()
customer2.name="Steve"
customer2.lastName="Rogers"
customer2.age=40
customer2.addCart()

customer3=Customer()
customer3.name="Tom"
customer3.lastName="Holland"
customer3.age=28
customer3.addCart()

customer4=Customer()
customer4.name="Salmon"
customer4.lastName="Sasimi"
customer4.age=10
customer4.addCart()
