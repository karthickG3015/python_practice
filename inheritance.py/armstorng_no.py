num = input("armstorng number: ")
j = 0

for i in num:
    k = pow(int(i) , len(num))
    j = j + k

if int(num) == j:
    print("it is armstorng")
else:
    print("it is not armstrong")





