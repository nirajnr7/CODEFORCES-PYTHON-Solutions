n=list(input())
dusra=[]
for i in n:
    
    if i not in "AEIOUaeiou":
        dusra.append(i)
        

           
answer=""

for i in dusra:
    answer+='.'
    answer+=i.lower()
print(answer)
        
        