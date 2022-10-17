def count(word):
    new_word = word
    count_syllables = new_word.split('-')
    return len(count_syllables)
        
obj = count('in-con-spic-ious')
print(obj)

