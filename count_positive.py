def count_positive(numbers):
    count=0
    for x in numbers:
        if x>0:
            count+=1
    return count 
results = count_positive([5,-2,8,-1,3])
print(results)            