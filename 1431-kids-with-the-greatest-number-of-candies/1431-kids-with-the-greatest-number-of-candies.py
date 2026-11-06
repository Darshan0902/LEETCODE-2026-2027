class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        res = [False] * len(candies)
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res[i] = True
            else:
                res[i] = False
        return res