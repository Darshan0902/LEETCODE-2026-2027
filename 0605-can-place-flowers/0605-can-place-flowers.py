class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length_flowerbed = len(flowerbed)
        for i in range(0,length_flowerbed):
            left = (i == 0 or flowerbed[i-1] == 0)
            right = (i==length_flowerbed-1 or flowerbed[i+1] == 0)
            curr  = flowerbed[i] == 0
            if left and right and curr:
                flowerbed[i]  = 1
                n-=1
            if n<=0:
                return  True
        return n<=0
        
