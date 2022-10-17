def only_ints(a, b):
    if type(a) == int and type(b) == int:
        return True
    else:
        return False

obj5 = only_ints('5', 4)
print(obj5)
