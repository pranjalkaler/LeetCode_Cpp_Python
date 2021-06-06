class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list("aeiouAEIOU")
        stack = []
        s = list(s)
        for x in s:
            if x in vowels:
                stack.append(x)
        
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = stack.pop()
        return "".join(s)
