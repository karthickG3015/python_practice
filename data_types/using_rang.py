# previous_no = 0

# for i in range(10):
#     sum = previous_no + i
#     print("current number", i ,"previous number", previous_no ,"The sum is: ", sum)
#     previous_no = i


# # # Print characters from a string that are present at an even index number # # #

# str = "pynative"

# for i in range(len(str)):
#     if i%2 == 0:
# # for i in range(0,len(str),2):
#         print(str[i])

word = input('Enter word : ')
x = word
for i in x[0::2]:
    print(i)

# word = input('Enter word: ')
# size = len(word)

# for i in range(0, size, 2):
#     print("index[", i, "]", word[i])