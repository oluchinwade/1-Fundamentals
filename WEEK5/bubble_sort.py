unsorted_list = [23,17,29,54,78,1,92,4]
def bubblesort(the_list):
    high_idex = len(the_list)-1

    for i in range(high_idex):
        for j in range(high_idex):
            item = the_list[j]
            next = the_list[j+1]

            if item > next:
                the_list[j] = next
                the_list[j+1] = item
            print(the_list, i,j)


print(bubblesort(unsorted_list))