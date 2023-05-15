def big(ls):
    new_ls=[]
    count=0
    if len(ls)==2:
        return min(ls)
    for i in ls:
        if count%2==0:
            new_ls.append(max(int(ls[count]),int(ls[count+1])))
        count+=1
    return big(new_ls)
ls=[]
ls.append(input().split())
for i in ls:
    ls=i
n=big(ls)
print(ls.index(str(n))+1)
            
            
    

