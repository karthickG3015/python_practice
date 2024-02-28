def first_and_last(numberlist):
    print("the list is: ",numberlist)

    first_num = numberlist[0]
    last_num = numberlist[-1]

    if first_num == last_num:
        return True
    else:
        return False
    
number_x = [10, 20, 30, 40, 10]
number_y = [75, 65, 35, 75, 30]
print("the result is ", first_and_last(number_x))
print("the result is ", first_and_last(number_y))