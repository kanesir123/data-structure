class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=n+m-1
        if m==0:
            nums1=nums2
        while i-m>=0 and m:
            if nums1[i-n]>nums2[i-m]:
                nums1[i],nums1[i-n]=nums1[i-n],nums1[i]
                m-=1
            else:
                nums1[i]=nums2[i-m]
                n-=1
            i-=1
        return nums1
nums1=[0]
nums2=[1]
m=0
n=1
print(Solution().merge(nums1,0,nums2,1))
