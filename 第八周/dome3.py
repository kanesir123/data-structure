def two_squence(ls):
    ls1=[]
    n=len(ls)
    i=0
    while n!=i:
        max_value=ls[0]
        min_value=ls[0]
        if i%2==0:
            for j in range(1,len(ls)):
                if ls[j]>max_value:
                    max_value=ls[j]
            ls.remove(max_value)
            ls1.append(max_value)
        else:
            for j in range(1,len(ls)):
                if ls[j]<min_value:
                    min_value=ls[j]
            ls.remove(min_value)
            ls1.append(min_value)
        i+=1
    return ls1
ls=[]
n=int(input())
for i in range(n):
    ls.append(int(input()))
m=two_squence(ls)
for j in m:
    print(j)
            
