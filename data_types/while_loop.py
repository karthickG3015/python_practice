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
        

correct = "O.P.S"
chances = 3
count = 0
special_character = ["!","@","#","*","()",")","&"]
while count < chances:
    k = input("enter the name = ")
    if k.isdigit() or k in special_character:
        print("You enter wrong")
        break
    else:
        count += 1
        if k == correct:
            print("You Won!")
            break
        