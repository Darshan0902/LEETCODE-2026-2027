class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = 0
        new_list = []
        n= len(candies)
        for i in range(0,n):
            if max_candies<candies[i]:
                max_candies = candies[i]
        for i in range(0,n):
            if candies[i]+extraCandies >= max_candies:
                new_list.append(True)
            else:
                new_list.append(False)
        return new_list
