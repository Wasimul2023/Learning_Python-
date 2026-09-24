def check_password(password):
    if len(password)>=8:
        results = "stong"
    else:
        results = "weak"
    return results
x = check_password("python1234")
print(x)
    