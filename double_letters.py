# from collections import Counter

# def double_letters(string):
#     wc = Counter(string)

#     for letter, count in wc.items():
#         if count < 1:
#             print(letter)
#             return False
#         else:
#             return True

# obj6 = double_letters('hahad')

# print(obj6)
# def double_letters(word):
#     for i in range (len(word)-1):
#         if word[i] == word[i+1]:
#             return True
#     return False

# print(double_letters("greet"))

def double_letters(string):
    for i in range(len(string) - 1):
        letter1 = string[i]
        letter2 = string[i+1]
        if letter1 == letter2:
            return True
    return False
obj = double_letters('stret')
print(obj)