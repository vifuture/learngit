s=str(raw_input("Enter strings:"))
x=0
i=0
for char in s:
    if(s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U'):
        x+=1
    i+=1
        
print(x)
