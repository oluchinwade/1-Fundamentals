def linear_search_dictionary(dictionary, target):
    for i, j in dictionary.items():
        if j == target:
            print("Found at key", i)
            return j
        
    print("Target is not in the dictonary")
    return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
