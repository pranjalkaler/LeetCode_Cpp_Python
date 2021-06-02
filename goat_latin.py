class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        ma = 'ma'
        a = 'a'
        vowels = list("aeiouAEIOU")
        words = sentence.split(" ")

        for i in range(len(words)):
            w = list(words[i])
            if w[0] not in vowels:
                w.append(w.pop(0))
            w.append(ma)
            w.append(a*(i+1))
            words[i] = "".join(w)
        return (" ".join(words)).strip()
