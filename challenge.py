name = input("Enter the name ")
age = int(input("Enter Age"))
marks = int(input("Enter Marks"))
if marks>=80:
    marks= "excellent"
elif 60>=marks<=79:
    marks = "Good"
elif 40>=marks<=59:
    marks = "Pass"
else:
    marks = "fail" 

print(name,"Your are",marks)