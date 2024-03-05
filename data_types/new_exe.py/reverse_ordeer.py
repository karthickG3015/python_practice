# num = 7536
# print("given number is: ",num)

# for i in str(num):
#     reverse_num = num % 10
#     num = num // 10
#     print(reverse_num, end=" ") 

### using while loop ###

x = int(input("the given number is: "))
y = 0
while x > 0 :
    reverse_num = x % 10
    x = x // 10
    #y = y*10 + reverse_num
    print(reverse_num, end=" ")