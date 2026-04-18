class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverseNum(x):
            rev=0
            while x > 0 :
                digit = x % 10  
                rev = rev * 10 + digit
                x = x // 10
            return rev
            
        return abs(n - reverseNum(n))