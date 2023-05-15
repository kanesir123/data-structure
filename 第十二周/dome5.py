m=int(input())
ls=[]
ls.append(input().split())
for i in ls:
    ls=i
import heapq
h=[]
for e in ls:
    heapq.heappush(h,int(e))
count=0
while m-1:
    p,q=heapq.heappop(h),heapq.heappop(h)
    a=p+q
    count+=a
    heapq.heappush(h,a)
    m-=1
print(count)
    
