class Solution:
    def checkString(self, s: str) -> bool:
        count=0
        for chars in s:
            if chars == "a":
                count+=1
        if count==0:
            return True
        
        if "b" in s[:count]:
            return False
        return True