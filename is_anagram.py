def is_anagram(par1, par2):
    if (sorted(par1) == sorted(par2)):
        return True
    else:
        return False

obj = is_anagram('word', 'draw')
print(obj)