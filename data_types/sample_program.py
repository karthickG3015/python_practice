std_list = ["jeeva" , "karthi" , "gokul" , "karthi" , "kaayadh" , "arun" , "bala" , "karthick"]

# sorting the std_list 
sort_list = sorted(std_list)
print("the sort list is: ", sort_list)

# find the duplicates in the std_list
count_list = std_list.count("karthi")
print(count_list)

# find and remove the duplicates(it will remove only one duplicate)
remove_list = list(set(sort_list))
print("remove duplicates: ", remove_list)

# reverse the remove list (it will print the list in the reverse order)
remove_list.reverse()
print("reverse the sorted list: ", remove_list)

# finding the index of the element
index_of_list = std_list.index("bala")
print("the index of the std_list is: ", index_of_list)

# update the std_list eleme
std_list[2] = "dead"
print("update the list: ", std_list)



