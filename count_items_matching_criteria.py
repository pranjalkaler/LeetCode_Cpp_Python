class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        mp = { "type" : 0, "color" : 1, "name" : 2 }
        key = mp[ruleKey]
        count = 0
        res = [ruleValue for tpl in items if tpl[key] == ruleValue ]
        return len(res)
        