marks=int(input("Enter the marks:"))
if marks>=90:
   grade="A+"
elif marks>=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    grade="c"
elif marks>=40:
   grade="D"
else:
    grade="F"
print(marks,"=",grade)