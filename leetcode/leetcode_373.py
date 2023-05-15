class Solution:
    def kSmallestPairs(self, nums1, nums2, k) -> list:
        # 请完善本函数定义体即可
        ls=[]
        m=min(len(nums1),k)
        n=min(len(nums2),k)
        for i in nums1[:m]:
            for j in nums2[:n]:
                heapq.heappush(ls,(i+j,i,j))
        h=[]
        while len(h)<min(k,len(nums1)*len(nums2)):
            a=heapq.heappop(ls)
            h.append(list(a[1],a[2]))
        return h
            
