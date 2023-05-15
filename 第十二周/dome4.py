import time
t1=time.perf_counter()
q=int(input())
ls=[]
new_ls=[]
for i in range(q):
    ls.append(input())
    if ls[i][0]=='1':
        new_ls.append(int(ls[i][2:]))
    elif ls[i][0]=='2':
        print(min(new_ls),end=' ')
    elif ls[i][0]=='3':
        new_ls.remove(min(new_ls))
t2=time.perf_counter()
print(t2-t1)
        
    
        
