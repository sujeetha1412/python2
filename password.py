text=input("enter a string:")
result=""
for i in range(0,len(text),2):
    letter=text[i]
    num=int(text[i+1])
    result+=letter*num
print(result)
[25bcs165@mepcolinux ex2]$cat password.py
password=input("enter password:")
if len(password)<8 or len(password)>15 or " " in password:
    print("invalid password")
elif not any(ch.isdigit() for ch in password):
    print("invalid password")
elif not any(ch.islower() for ch in password):
    print("invalid password")
elif not any(ch.isupper() for ch in password):
    print("invalid password")
elif not any(ch in "@#$%&!*." for ch in password):
    print("invalid password")
else:
    print("valid password")
