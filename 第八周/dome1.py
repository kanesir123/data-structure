def Equlity(ls,n):
    ls.sort()
    for i in range(1,n):
        if ls[i]==ls[i-1]:
            return 'Yes'

    return 'No'
n=int(input())
ls=list(map(int,input().split()))
Equlity(ls,n)
