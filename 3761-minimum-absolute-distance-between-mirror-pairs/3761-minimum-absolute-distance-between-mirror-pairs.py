class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverseNum(i):
            rev=0
            while i > 0:
                rev = rev * 10 + i % 10
                i = i // 10
            return rev
        
        mp={}
        ans= float('inf')

        for j in range(len(nums)):
            if nums[j] in  mp:
                ans = min(ans,j - mp[nums[j]])
            rev = reverseNum(nums[j])
            mp[rev] = j
        
        return -1 if ans == float('inf') else ans