import re

def flatten(list):
    result = []
    for sublist in list:
        sublist = re.sub('[\[\]]','',repr(list)) 
        result.append(sublist)
        for l in result:
            l = str(result)
        return l

obj = flatten([[1, 2], [3, 4], [5, 6]])
print(obj.replace("'", ""))