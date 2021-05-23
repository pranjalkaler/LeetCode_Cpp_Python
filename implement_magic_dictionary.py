class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:

        for word in self.words:
            if len(word) == len(searchWord):
                diffCount = 0
                for i in range(len(word)):
                    if word[i] != searchWord[i]:
                        diffCount += 1
                if diffCount == 1:
                    return True
        
        if searchWord in self.words:
            return False
        
        return False
# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)