n=int(input())
answer=0
for _ in range(n):
    t=input()
    
    if '++' in t:
        answer+=1
    elif '--' in t:
        answer-=1
print(answer)
    