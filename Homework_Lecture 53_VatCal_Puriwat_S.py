print("This is Vat Calculator")
print("Please input price for calculating vat ")
PDPrice=float(input("Product Price (THB) : "))

vat= 7/100
def VatCal(PDPrice):
    TotalPrice=PDPrice+(PDPrice*vat)
    return  TotalPrice

print("from Price before VAT : ",PDPrice,"THB")
print("if VAT percentage is ",int(vat*100),"%")
print("---------------------------------------")
print("Total product price will be :",VatCal(PDPrice),"THB" )


