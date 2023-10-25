def binary_search(the_list, target):
    lower_bound = 0
    upper_bound = len(the_list)-1

    while lower_bound <= upper_bound:
        pivot = (lower_bound+upper_bound)//2
        #this shows the index value []
        pivot_value = the_list[pivot]

        if pivot_value == target:
            return pivot
        if pivot_value > target:
            upper_bound = pivot -1
        else:
            lower_bound = pivot +1
    
    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
target= 4
print(binary_search(my_list, target))