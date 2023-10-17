ingredients = {'flour':'1.5 cups', 'sugar':'1.5 cups'}
print(ingredients['flour'])
print(len(ingredients))
ingredients['flour'] = '3.5 cups'
ingredients['egg'] = '3'
print(ingredients)
print("Here are the ingredients needed to make Pancakes")
for s in (ingredients):
    print(s)
    print(ingredients[s])
for t in ingredients.values():
    print(t)
for i,j in ingredients.items():
    print(f"For {i} you will need {j} ")
