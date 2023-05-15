class Solution:
    def groupAnagrams(self, strs):
        ls=[]
        i=0
        while i<len(strs):
            ls1=[]
            ls1.append(strs[i])
            a=sorted(strs[i])
            j=i+1
            while j<len(strs):
                if a==sorted(strs[j]):
                    ls1.append(strs[j])
                    strs.pop(j)
                    j-=1
                j+=1
            i+=1
            ls.append(ls1)
        return ls
strs = ["","b",""]
print(Solution().groupAnagrams(strs))
