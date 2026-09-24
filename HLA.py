salaries = [25000, 32000, 28000, 45000, 22000, 50000, 35000]
big= salaries[0]
small = salaries[0]
addition= 0
count = 0
for x in salaries:
    if x>=big:
        big =x
    if x< small:
        small = x
    addition+=x
    avg = addition/len(salaries)
    if x>=30000:
        count+=1
        

print("Highest Salary :",big)
print("Lowest salary :",small)
print("Average :",avg)
print("30K or Above :",count)

