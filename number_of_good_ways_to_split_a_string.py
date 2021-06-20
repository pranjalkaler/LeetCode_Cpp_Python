class Solution:
    def numSplits(self, s: str) -> int:
        s = list(s)
        left_dict = {}
        right_dict = {}
        left_dict[s[0]] = 1
        
        for i in range(1, len(s)):
            right_dict[s[i]] = right_dict[s[i]] + 1 if s[i] in right_dict.keys() else 1
        
        left = 1
        right = len(right_dict)
        count = 0 if left != right else 1
        for i in range(1, len(s) - 1):
            left_dict[s[i]] = left_dict[s[i]] + 1 if s[i] in left_dict.keys() else 1
            right_dict[s[i]] -= 1
            if right_dict[s[i]] == 0:
                del right_dict[s[i]]
            left = len(left_dict)
            right = len(right_dict)
            if left == right:
                count += 1
        return count
