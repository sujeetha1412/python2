text=input("enter a string:")
if len(text)<3:
    result=text
elif text[-3:]=="ing":
    result=text+"ly"
else:
    result=text+"ing"
print(result)
[25bcs165@mepcolinux ex2]$cat letter.py
text=input("enter a string:")
result=""
for i in range(0,len(text),2):
    letter=text[i]
    num=int(text[i+1])
    result+=letter*num
print(result)
