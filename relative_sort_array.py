class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        Dict = {}
        for x in arr1:
            Dict[x] = Dict[x] + 1 if x in Dict.keys() else 1
        result = []
        for x in arr2:
            result.extend([x] * Dict[x])
            del Dict[x]
        for x in sorted (Dict.keys()):
            result.extend([x] * Dict[x])
        print(result, Dict)
        return result