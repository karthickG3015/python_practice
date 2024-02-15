# using distionary


# creating a dictionary
dect1 = {}
print(dect1)
print(type(dect1))

dect2 = {1:"welcome", 2:"to", 3:"my", 4:"world"}
print(dect2)

dect3 = {"name":"bharath" , "age":28 , "profession":"python QA"}
print(dect3)

dect4 = ({1:"welcome",2:"to",3:"new",4:"new",5:"world"})
print(dect4)

dect5 = dict([(1,"welcome"),(2,"to"),(3,"python")])
print(dect5)

# adding elements
d = {}
d[0] = "welcome"
print(d)
d[1] = ("How","are","you")          # add tuple in the dictionary
print(d)
d["name"] = "sam"                   # adding dict
print(d)
d["name"] = {"first":"sam" , "last":"santhosh"}     # update dict
print(d)

# accessing elements
print(d["name"])
print(d["name"]["last"])            # access nested dict
print(d.get(0))                     # using get()

# deleting elements
# d.pop(0)                            # deleting the perticular element
# print(d)
# d.popitem()                         # deleting the last element of dict
# print(d)

# using built-in fuctions
k = d.values()
print(k)

keys = ("a","b","c","d","e")
value = "o gaya"
g = dict.fromkeys(keys,value)                               # using  built in function to create the dict
print(g)

keys = (1,2,3,4,5)
value = ("why", "are", "you", "learn" , "python")
m = zip(keys,value)                                         # using  built in function to create the dict
print(dict(m))



