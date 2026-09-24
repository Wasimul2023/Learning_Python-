def calculate_grade(marks):
    if marks>=80:
        grade ="A"
    elif marks>=70:
       grade="B"
    elif marks>=60:
           grade="C"
    else:
        grade="F"
    return grade 
x = calculate_grade(65)
print(x)
    

