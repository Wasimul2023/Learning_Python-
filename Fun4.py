def count_even(n):
    i= 1 
    count = 0
    while i<=n:
        if i%2==0:
            count+=1
        i +=1
    return count
results= count_even(10)
print(results)
