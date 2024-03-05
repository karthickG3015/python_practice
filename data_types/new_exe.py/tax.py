# income = 45000
# print("the income of:", income)

# total=(10000*(0/100))+(10000*(10/100))+(25000*(20/100))
# print("the total tax pay is: ",total)

### using if condition ###
income = 45000
tax_payable = 0

if income <= 10000:
    tax_payable = 0
    print("tax to 0% : ", tax_payable)
elif income <= 20000:
    tax_payable  = income - 10000
    print("tax to 10% : ", tax_payable)
else:
    tax_payable = (10000 *(0/100)) +(10000*(10/100))+ ((income-20000)*(20/100))
    print("tax to 20% : ", tax_payable)
