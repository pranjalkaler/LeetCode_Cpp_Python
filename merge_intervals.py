class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        
        # [[1, 3], [2, 6], [8, 10], [15, 18]]
        stack = []
        for interval in intervals:
            if not stack:
                stack.append(interval)
            else:
                last = stack[-1]
                if last[1] >= interval[0]:
                    last = stack.pop()
                    start = min(last[0], interval[0])
                    end = max(last[1], interval[1])
                    interval = [start, end]
                stack.append(interval)
        # print(stack)
        return stack
