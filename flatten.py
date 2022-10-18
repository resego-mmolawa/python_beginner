import re

def flatten(list):

    result = []
    for sublist in list:
        for element in sublist:
            result.append(element)
    return result

obj = flatten([[1, 2], [3, 4]])
print(obj)
