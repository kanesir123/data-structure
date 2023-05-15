
n,q=map(int,input().split())
ls=list(input().split())
ls1=list(input().split())
ls2=[]
for i in ls1:
    try:
        ls2.append(str(ls.index(i)))
    except:
        ls2.append('-1')
        
    
print(''.join(ls2))

            
    
