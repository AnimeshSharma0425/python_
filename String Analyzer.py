string=input("enter a string:")
vowels=0
consonents=0
spaces=0
digits=0
for i in string:
    if i.lower() in "aeiou":
        vowels+=1
    elif i.isalpha():
        consonents+=1 
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
print(f"vowels:{vowels}\nconsonents:{consonents}\ndigits:{digits}\nspaces{spaces}")