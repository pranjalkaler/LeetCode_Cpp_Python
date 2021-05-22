class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        result = []
        i = 0
        last = ""
        second_last = ""
        for word in text:
            if last == second and second_last == first:
                result.append(word)
            second_last = last
            last = word
        return result
