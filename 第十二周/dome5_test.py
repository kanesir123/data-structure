import heapq
class Solution:
    def maxKelements(self, nums: list, k: int) -> int:
        # 请完善本函数定义即可
        count=0
        h=[]
        for e in nums:
            heapq.heappush(h,-e)
        while k:
            a=heapq.heappop(h)
            heapq.push(h,a//3)
            count+=a
            k-=1
        return -count

ls=list(map(int,input().split()))
k=int(input())
t1=time.perf_counter()
print(maxKelements(ls,k))
t2=time.perf_counter()
print(t2-t1)

    

