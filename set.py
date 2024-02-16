# sets

set_op = set([1,2,3,4,5])
print(set_op)

set_op.add("new")                   # adding a set
print(set_op)

fs = frozenset([1,2,3,4,"baby"])           # frozenset
print(fs)

s1 = set([1,4,6,8,9,4,5])
s2 = set([2,4,6,8,9,5,3])
a = s1.union(s2)
b = s1.difference(s2)
sum_of = sum(s1)
print("the sum of the set is:", sum_of)
print(a)
print(b)

# operators with sets

check_condi = s1 == s2
print(check_condi)

check_condi = s1 > s2
print(check_condi)

check_condi = 1 in s1
print(check_condi)

check_condi = 61 in s1
print(check_condi)

check_condi = 1 not in s1
print(check_condi)

check_condi = s1 ^ s2
print(check_condi)