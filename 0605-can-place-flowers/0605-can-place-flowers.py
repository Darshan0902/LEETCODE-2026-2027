class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        n1 = len(flowerbed)
        le = re = 0
        for i in range(0,n1):
            if i == 0 or flowerbed[i-1] == 0:
                le = True
            if i == n1-1 or flowerbed[i+1] == 0:
                re = True
            if le and re and  flowerbed[i] == 0 and n > 0:
                flowerbed[i] = 1
                n-=1
                le = re = 0
            else:
                le=re=0
        if n <= 0:
            return True 
        else:
            return False