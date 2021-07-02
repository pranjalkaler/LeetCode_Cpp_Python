class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalids = ['3', '4', '7']
        rotation = {
            '1' : '1',
            '2' : '5',
            '5' : '2',
            '6' : '9',
            '8' : '8',
            '9' : '6',
            '0' : '0'
        }
        
        count = 0
        for i in range(n+1):
            num = list(str(i))
            rev = []
            flag = False
            for digit in num:
                if digit in invalids:
                    flag = True
                    break
                else:
                    rev.append(rotation[digit])
            if not flag:
                reverse = int("".join(rev))
                if reverse != i:
                    count += 1
        return count
