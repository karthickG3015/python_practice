# #i = 1
# #while i <= 5:
# #    print("*" * i)
# #    i += 1
# #print("Done")




# currect_ans = "O.P.S"
# attement_count = 0
# attement_limit = 3
# while attement_count < attement_limit:
#     guess = (input("21-09-2001 to 01-03-2002 who is the CM of TamilNadu: "))
#     attement_count += 1

#     if guess == currect_ans:
#         print("you won!")
#         break
# else:
#     print("sorry, you failed!")
        

# correct = "O.P.S"
# chances = 3
# count = 0
# special_character = ["!","@","#","*","()",")","&"]
# while count < chances:
#     k = input("enter the name = ")
#     if k.isdigit() or k in special_character:
#         print("You enter wrong")
#         break
#     else:
#         count += 1
#         if k == correct:
#             print("You Won!")
#             break

# i = 0
# while i < 10:
#     i += 1
#     print(i, end="#")
#     print()

# while True:
#     print("please type your name")
#     name = input()
#     if name == "karthi":
#         break
# print("thank you, you enter the correct name")

# finding the least common multiple of 4 and 7
# x = 0
# while True:
#     x += 1
#     if not(x%4 or x%7):
#         break
# print(x)

# i = 0
# while i < 10:
#     i += 1
#     if i == 6:
#         continue
#     print(i)

# i = 1 
# while i < 5:
#     print(i)
#     i += 1
# else:
#     print("i is not less than 5")

# positive number
# num = 0 
# count = 0 
# sum = 0

# while num >= 0:
#     num = int(input("enter the positive number: "))
#     if num >= 0:
#         count = count + 1
#         sum = sum + num
# avg = sum / count
# print("sum of the number: ", sum, "avarage: ", avg)

# random numbers
import random
n = random.randint(1 , 100)
print(n)
guess = int(input("enter an integer between 1 to 100: "))

while guess != n:
    if guess < n:
        print("your guess is low")
        guess = int(input("enter an interger between 1 to 100: "))
    elif guess > n:
        print("your guess is high")
        guess = int(input("enter an integer between 1 to 100: "))
else:
    print("your guess is correct")
    
    










