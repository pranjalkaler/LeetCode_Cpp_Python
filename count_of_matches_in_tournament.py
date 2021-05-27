class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n >= 2:
            if n % 2 == 0:
                count += int(n/2)
                n = int(n/2)
            else:
                count += int((n-1)/2)
                n = int(n/2) + 1
        return count
