def ProductOfTwo (num1 , num2):
    product = num1 * num2

    if product <= 1000:
        return product
    else:
        return num1 + num2
    
result = ProductOfTwo(101,10)
print(result)
