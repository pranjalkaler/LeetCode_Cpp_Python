class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_map = [".-","-...","-.-.","-..",".",
                     "..-.","--.","....","..",".---",
                     "-.-",".-..","--","-.","---",
                     ".--.","--.-",".-.","...","-",
                     "..-","...-",".--","-..-","-.--","--.."]
        result = set()
        
        for word in words:
            code = ""
            for letter in word:
                code += morse_map[ord(letter) - 97]
            result.add(code)
        return len(result)
