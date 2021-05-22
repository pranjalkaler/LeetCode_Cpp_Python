class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def generateHash():
            Hash = {}
            for char in chars:
                Hash[char] = Hash[char] + 1 if char in Hash.keys() else 1
            return Hash
        count = 0
        for word in words:
            flag = False
            tempHash = generateHash()
            for char in word:
                if char not in tempHash.keys() or tempHash[char] == 0:
                    flag = True
                else:
                    tempHash[char] -= 1
            if not flag:
                count += len(word)
        return count
