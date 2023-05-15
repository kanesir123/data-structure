class Solution:
    def permute(self, nums):
        ls=[]
        for i in range(len(nums)):
            ls1=[]
            ls1.append(nums[i])
            nums1=nums[:i]+nums[i+1:]
            def Num(nums1):
                if len(nums1)==1:
                    return nums[0]
                for j in range(len(nums1)):
                    ls1.append(nums1[j])
                    nums2=nums1[:j]+nums[j+1:]
                    ls1.append(Num(nums2))
                    ls.append(ls1)
        Num(nums)
        return ls
nums = [1,2,3]
print(Solution().permute(nums))
