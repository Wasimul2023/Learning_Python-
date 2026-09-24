numbers=[12,7,20,15,30,9,40]
sum=0
odd_sum=0
for x in numbers:
    if x%2==0:
        sum+=x
    else:
        odd_sum+=x
    
print(sum)
print(odd_sum)