# Find the largest number
# numbers = [322, 450, 890, 550, 999, 220, 934, 303]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

    # 2D list
# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# matrix [1][1] = 20
# print(matrix)

# matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# for row in matrix:
#     for iteam in row:
#         print(iteam)

# numbers = [4, 8, 12, 16, 4, 12, 20]
# uniques = []
# for number in numbers:
#     if number not in uniques:
#         uniques.append(number)
# print(uniques)

# x = ["java", "python", "c++", "C"]
# for i in range(len(x)):
#     print("Hello", x[i])

# player_name = "karthick"
# goals = {"jeeva": 2, "manoj": 5, "karthick": 8}
# for player in goals:
#     if player == player_name:
#         print(goals[player])
#         break
# else:
#     print("no player name found")

# find the cube values of the list
# num = [2,5,8,12,90]
# cube = []
# for i in num:
#     cube.append(i**3)
# print(cube)

# pattern printing
n = int(input("Enter the no's of rows:" ))
for i in range(0,n):
    for j in range(0, i+1):
        print("*", end=" ")
    print()