def reverse(a):
    rev_name =""
    for i in reversed(a):
        rev_name += i
    return rev_name

a = "Olibaby"

print(f"Your reversed name is: {reverse(a)}")