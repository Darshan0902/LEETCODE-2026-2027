class Solution:
    def compress(self, chars: list[str]) -> int:
        n= len(chars)
        i  = 0
        write= 0
        while i <n:
            char = chars[i]
            count =  0
            while i < n and chars[i] == char:
                count+=1
                i+=1
            chars[write] = char
            write+=1
            if count > 1:
                for digit in (str(count)):
                    chars[write] = digit
                    write+=1
        return write
