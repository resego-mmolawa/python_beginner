def add_dots(string):
    x = '.'.join(string[i:i + 1] for i in range(0, len(string), 1))
    return x

def remove_dots(string):
    x2 = string.replace('.', '')
    return x2

obj1 = add_dots('test')
obj2 = remove_dots('t.e.s.t')

print('results after adding dots is', obj1)
print('results after adding dots is', obj2)