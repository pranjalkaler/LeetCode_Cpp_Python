class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode('*')

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for x in word:
            if not node.children:
                node.children = [ None ] * 26
            if not node.children[ord(x) - 97]:# == ' ':
                node.children[ord(x) - 97] = TrieNode(x)
            node = node.children[ord(x) - 97]
        node.is_last_letter = True
            
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for x in word:
            if not node.children or not node.children[ord(x) - 97]:
                return False
            node = node.children[ord(x) - 97]
        return node.is_last_letter
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for x in prefix:
            if not node.children or not node.children[ord(x) - 97]:
                return False
            node = node.children[ord(x) - 97]
        return True
        
    
class TrieNode:
    def __init__(self, letter='#', is_last_letter=False):
        self.letter = letter
        self.is_last_letter = is_last_letter
        self.children = []

    def __str__(self):
        return "{}, {}, {}".format(self.letter, self.is_last_letter, self.children)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
