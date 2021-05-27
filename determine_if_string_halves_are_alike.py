class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        length = len(s)
        half = int(length/2)
        str1, str2 = s[0:half], s[half:length]
        v1 = v2 = 0
        for x in str1:
            if x in vowels:
                v1 += 1
        for x in str2:
            if x in vowels:
                v2 += 1
        return v1 == v2
