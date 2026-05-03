class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a" , "e" , "i" , "o"  , "u" , "A" ,"E"  ,"I" , "O" , "U"]
        sl =  list(s)
        l = 0
        r  =len(sl)-1
        while l < r:
            if sl[l] in  vowels and sl[r] in vowels:
                sl[l],sl[r] = sl[r],sl[l]
                l+=1
                r-=1
            elif sl[l] not in vowels:
                l+=1
            elif sl[r] not in vowels:
                r-=1
        return "".join(sl)