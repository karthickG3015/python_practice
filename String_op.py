# String

name = "bharath is a playboy"
print(len(name))
print(name[10])

# for i in name:
#     #print(i)
#     print(i,end="")

# slicing
print(name[0:6])
print(name[10:])
print(name[:6])
print(name[9:10])

print(name.upper())
print(name.lower())
print(name.find("i"))
print(name.index("p"))
# print(name.split(" "))
g = name.split(" ")                         # It will be retrun a list
print(g)

print(name.replace("playboy" , "playGod"))
print(name.rpartition(" is "))
