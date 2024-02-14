# using tuples

emp = ()                # empty tuple
print(emp)      
city = ("chennai", "mumbai", "bangalore", "delhi")
num = (1,2,3,8,9,5,3,3,3,4)
print(city+num)                # concatenation
nest = (emp,num,city)           # nesting
print(nest)
rep = ("python",)*5             #repetition
print(rep)                  # (or) print(rep*5) there are same
# del emp                   # delete the tuples
# print(emp)
num1 = (1,2,3,8,9,5,3,3,3,4)
k = num1.count(3)           # count the number of variable
print(k)
A = sum(num1)               # sum of the varable
print(A)
B = len(num)                # finding lenth of the variable 
print(B)
a = min(num1)               # minimum number of the variable
print(a)
b = max(num1)               # maximum number of the variable
print(b)
c = sorted(num1)             # sorted the tuple variable
print(c)
my_list = [3,4,1,4,4,3,9,6,8,5]
print(my_list)
print(type(my_list))
my_tuple = tuple(my_list)           # convert to tuple
print(my_tuple)
print(type(my_tuple))
new_list = [(1,2,3),(4,5,6)]                    # nesting tuple within list
new_list.append(("list","tuple","insert"))         
print(new_list)
new_list.remove((1,2,3))
print(new_list)
new_tuple = (["x","y","z"],["a","b","c"])       # nesting list within tuple
print(new_tuple)
new_tuple[1].append("Z")
print(new_tuple)
new_tuple[0].remove("z")
print(new_tuple)


series = (0,1,2,3,4,5,6,7,8,9)
print(series)
series1 = series+(10,11)
k = (10)
l = (10,)
print(series1)
print(type(k))
print(type(l))
print(type(series))
series2 = series1[:11]+series[::-1]
print(series2)