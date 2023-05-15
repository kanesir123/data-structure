import time
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 请补全本函数定义即可
        def uglyNumber(i):
            if i==1:
                return True
            if i%2==0:
                i=i//2
            if i%3==0:
                i=i//3
            if i%5==0:
                i=i//5
            if i%2!=0 and i%3!=0 and i%5!=0 and i!=1:
                return False
            return uglyNumber(i)
        ls=[]
        i=1
        while len(ls)<=n:
            if uglyNumber(i):
                ls.append(i)
                i+=1
            else:
                i+=1
        return ls[n-1]
t1=time.perf_counter()
print(Solution().nthUglyNumber(10))
t2=time.perf_counter()
print(t2-t1)
                
            
                
