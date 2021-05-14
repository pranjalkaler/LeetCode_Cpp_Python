class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        sm = 0
        while sm < 1 or sm > 9:
            sm = 0
            while num:
                digit = int(num % 10)
                sm += digit
                num = int(num/10)
            num = sm
        return sm