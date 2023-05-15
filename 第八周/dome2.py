n=int(input())
ls=list(input().split())
count=0
num=1
while num!=n:
    for i,j in enumerate(ls):
        if int(j)==num:
            count+=i
            ls.remove(j)
    num+=1
            
print(count)
    
