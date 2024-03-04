def palindrome_num (number):
    num_str = str(number)
    return num_str == num_str[::-1]

number = 12321
if palindrome_num(number):
    print(f"{number} is palindrome")
else:
    print(f"{number} is not palindrome")