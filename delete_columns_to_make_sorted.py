class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lists = [
            [
                x for x in strs[i]
            ] for i in range(len(strs))
        ]
        print(lists)
        count = 0
        for i in range(len(lists[0])):
            flag = False
            for j in range(len(lists) - 1):
                if lists[j][i] > lists[j+1][i]:
                    flag = True
            if flag:
                count += 1
        return count