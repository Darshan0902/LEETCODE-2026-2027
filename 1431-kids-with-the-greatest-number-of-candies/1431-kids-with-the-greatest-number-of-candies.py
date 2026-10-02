class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies=max(candies)
        res_list = []
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= max_candies:
                res_list.append(True)
            else:
                res_list.append(False)
        return res_list 

