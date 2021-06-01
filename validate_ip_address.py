import re

class Solution:
    def validIPAddress(self, IP: str) -> str:
        if ':' in IP:
            IP = IP.split(":")
            if len(IP) == 8:
                for seg in IP:
                    if seg:
                        valid_regex = '^[0-9a-fA-F]{1,4}$'
                        if not re.match(valid_regex, seg):
                            return "Neither"
                    else:
                        return "Neither"
                return "IPv6"
            else:
                return "Neither"
        elif '.' in IP:
            IP = IP.split(".")
            if len(IP) == 4:
                for seg in IP:
                    if seg:
                        try:
                            num = int(seg)
                            if num == 0:
                                if seg in ['00', '000']:
                                    return "Neither"
                            elif str(num) != seg or num > 255:
                                return "Neither"
                        except:
                            return "Neither"
                    else:
                        return "Neither"
                return "IPv4"
            else:
                return "Neither"
        return "Neither"
