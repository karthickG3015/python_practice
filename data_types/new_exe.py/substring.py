### Write a program to find how many times substring “Emma” appears in the given string ###
### using count() method ###

# str = "Emma is good developer. Emma is a writer"
# x = str.count("Emma")
# print("Emma appeared", x ,"times")


### using without string method ###

def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement)):
        count += statement[i: i + 3] == "one"
    return count

count = count_emma("one-one was a race horse. Two-two was one too. one-one won one race. Two-two won one too.")
print("one appeared ", count, "times")