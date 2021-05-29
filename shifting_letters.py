class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prev = 0
        size = len(shifts)
        for i in range(size):
            shifts[size - 1 - i] += prev
            prev = shifts[size - i - 1]
        # print(shifts)
        s = list(s)
        for i, x in enumerate(s):
            shift = ord(x) - 97 + shifts[i]
            newPos = int(shift % 26)
            # print(i, x, shift, newPos)
            if shift:
                # print(newPos)
                newChar = chr(newPos + 97)
                s[i] = newChar
        return "".join(s)
