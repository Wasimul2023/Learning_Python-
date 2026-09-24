def count_vowel(word):
    count =0
    for x in word:
        if x in "aeiou":
             count+=1  
    return count
results = count_vowel("apple")
print(results) 

    