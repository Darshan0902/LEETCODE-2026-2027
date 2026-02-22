class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n  = len(nums)
        total_sum = sum(nums)
        left_sum=0
        for i in range(n):
            left_sum = sum(nums[:i])
            right_sum = total_sum - left_sum - nums[i]   
            if left_sum == right_sum:
                return i 
        return -1