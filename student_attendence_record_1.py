class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        late = 0
        for status in s:
            if status == 'A':
                absent += 1
                late = 0
                if absent >= 2:
                    return False
            if status == 'L':
                late += 1
                if late >= 3:
                    return False
            if status == 'P':
                late = 0
        return True
