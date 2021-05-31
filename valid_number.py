import re

class Solution:
    def isNumber(self, s: str) -> bool:
        def is_decimal(num):
            valid_regex = '^[+|-]*[0-9]*[.]{0,1}[0-9]*$'
            invalid_regex = '^[+|-]*[.]*$'
            return re.match(valid_regex, num) and not re.match(invalid_regex, num)
            
        def is_integer(num):
            valid_regex = '^[+|-]*[0-9]+$'
            return re.match(valid_regex, num)
        
        if 'e' in s:
            nums = s.split('e')
            if len(nums) > 2:
                return False
            return is_decimal(nums[0]) and is_integer(nums[1])
        elif 'E' in s:
            nums = s.split('E')
            if len(nums) > 2:
                return False
            return is_decimal(nums[0]) and is_integer(nums[1])
        else:
            return is_decimal(s)
        return re.match(regex, s)
