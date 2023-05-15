def low(item,ls):
    ls.sort()
    n=0
    for i in ls:
        if i<item:
            n+=1
    return n
class Solution:
    def reversePairs(self, nums: list) -> int:
        s=set(nums)
        n=len(s)
        ls=[0]*n
        ls1=[len(nums)]*n
        
        count=0
        for i in range(len(nums)-2,-1,-1):
            n=low(nums[i],nums[i:ls1[nums[i]]])+ls[nums[i]]
            count+=n
            ls[nums[i]]=n
            ls1[nums[i]]=i
        return count   
print(Solution().reversePairs([2147483647,2147483647,2147483647,2147483647,2147483647,2147483647]))
