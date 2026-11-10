class Solution:
    def reverseVowels(self, s: str) -> str:
        s1 = list(s)
        vowels= ["a","e","i","o","u","A","E","I","O","U"]
        l =0
        r = len(s) - 1
        while l < r:
            if s1[l] in vowels and s1[r] in vowels:
                s1[l],s1[r] = s1[r],s1[l]
                l+=1
                r-=1
            elif s1[l] in vowels:
                r -= 1
            elif s1[r] in vowels:
                l += 1
            else:
                l+=1
                r-=1
        return "".join(s1)