class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix =[1] * n
        res = [1]*n
        suffix= 1
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        for i in range(n-1,-1,-1):
            res[i] = prefix[i] * suffix
            suffix*=nums[i]
        return res