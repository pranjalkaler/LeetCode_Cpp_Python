class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        _1s = s.count('1')
        left = 1 if s[0] == '0' else 0
        right = _1s if s[0] == '0' else _1s - 1
        _max = left + right
        for i in range(1, len(s) - 1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            if left + right > _max:
                _max = left + right
        return _max
