text=input("enter a string:")
n=len(text)
print("All substrings are:")
for i in range(n):
    for j in range(i+1,n+1):
        print(text[i:j])
