class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dct = dict(Counter(arr))
        lst = [ x for x in dct.values() ]
        st = { x for x in dct.values() }
        return len(st) == len(lst)