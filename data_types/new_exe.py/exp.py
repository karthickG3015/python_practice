# def exponts(base , exp):
#     num = exp
#     result = 1
#     while num > 0:
#         result = result * base
#         num = num -1
#     print(result)
# exponts(5,4)

# def exponts (base , exp):
#     result = 1
#     while exp > 0:
#         result = result * base
#         exp = exp - 1
#     print(result)
# exponts(5,4)

base = int(input("the base is: "))
exp = int(input("the exponts is: "))

result = 1
while exp > 0:
    result = result * base
    exp = exp - 1
print(result)
