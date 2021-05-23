class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def getStrings(Digits):
            if len(Digits) == 0:
                return ""
            current_number = Digits.pop(0)
            subStrings = getStrings(Digits)
            this_node_letters = mapping[current_number]
            if len(subStrings) == 0:
                return list(this_node_letters)
            result = []
            # print("MAPPING: {}".format(this_node_letters))
            for letter in this_node_letters:
                for string in subStrings:
                    # print("{}{}".format(letter, string))
                    result.append("{}{}".format(letter, string))
            return result
        
        return getStrings(list(digits))
