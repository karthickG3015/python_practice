def ProductOfTwo (num1 , num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
    
result = ProductOfTwo(30,30)
print(result)
