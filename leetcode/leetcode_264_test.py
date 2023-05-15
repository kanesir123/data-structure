import time
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 请补全本函数定义即可
        ls=[1]
        i1,i2,i3=0,0,0
        count=0
        while count<=n:
            i=min(ls[i1]*2,ls[i2]*3,ls[i3]*5)
            if  i not in ls:
                ls.append(i) 
            if i==ls[i1]*2:
                i1+=1
            if i==ls[i2]*3:
                i2+=1
            if i==ls[i3]*5:
                i3+=1
            count+=1
        return ls[n-1]
t1=time.perf_counter()
print(Solution().nthUglyNumber(11))
t2=time.perf_counter()
print(t2-t1)
