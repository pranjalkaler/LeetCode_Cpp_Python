class Solution:
    def average(self, salary: List[int]) -> float:
        def Sort(arr):
            for i in range(1, len(arr)):
                j = i - 1
                key = arr[i]
                while j >= 0 and key < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1
                arr[j + 1] = key
        Sort(salary)
        _sum = 0
        for i in range(1, len(salary) - 1):
            _sum += salary[i]
        avg = _sum / (len(salary) - 2)
        return avg