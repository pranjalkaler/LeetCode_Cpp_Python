class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr):
            return max(arr)
        n1 = arr.pop(0)
        win_count = {}
        while True:
            n2 = arr.pop(0)
            if n1 > n2:
                arr.append(n2)
            else:
                arr.append(n1)
                n1 = n2
            win_count[n1] = win_count[n1] + 1 if n1 in win_count.keys() else 1
            # print(win_count)
            if win_count[n1] == k:
                return n1
