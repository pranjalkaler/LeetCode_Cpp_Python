class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_map = {}
        for email in emails:
            email = email.split("@")
            _local = ""
            local = list(email[0])
            while local and local[0] != '+':
                if local[0] != '.':
                    _local += local[0]
                local.pop(0)
            domain = email[1]
            email = _local + '@' + domain
            email_map[email] = email_map[email] + 1 if email in email_map.keys() else 1
        return len(email_map)
