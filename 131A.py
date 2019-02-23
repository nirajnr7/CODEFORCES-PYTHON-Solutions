n=input()

if len(n)==1 and n.islower():
    print(n.upper())

else:
    t=0
    for i in n:
        if i.isupper():
            t+=1
    
    if t==len(n):
        print(n.lower())