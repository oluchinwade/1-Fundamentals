def linear_search(the_list, target):
    for x in range(len(the_list)):
        if the_list[x] == target:
            print("found at index", x)
            return x
    print("Target is not in the list")
    return -1



my_list = [6,2,3,9,8]
linear_search(my_list,8)
linear_search(my_list,2)
linear_search(my_list,7) 