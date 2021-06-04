class Solution:
    def hammingWeight(self, n: int) -> int:
        def countOnes(num):
            count = 0
            for x in num:
                if x == '1':
                    count += 1
            return count

        def getBin(num):
            return bin(num)[2:] 

        # result = []
        # for i in range(n+1):
        #     result.append()
        # return result
        return countOnes(getBin(n))
