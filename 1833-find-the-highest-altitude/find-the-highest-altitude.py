class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_sum = 0
        curr_sum = 0
        n = len(gain)
        for i in range(0,n):
            curr_sum += gain[i]
            if curr_sum > max_sum:
                max_sum=curr_sum
        return max_sum

