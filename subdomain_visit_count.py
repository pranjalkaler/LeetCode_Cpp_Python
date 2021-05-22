class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        def get_sub_domain(domain):
            while domain and domain[0] != ".":
                domain.pop(0)
            if len(domain) > 0:
                domain.pop(0)
                return "".join(domain)
            return ""

        Hash = {}
        for val in cpdomains:
            val = val.split(" ")
            count, domain = val[0], val[1]
            Hash[domain] = Hash[domain] + int(count) if domain in Hash.keys() else int(count)
            subD = get_sub_domain(list(domain))
            # print(Hash)
            while subD:
                Hash[subD] = Hash[subD] + int(count) if subD in Hash.keys() else int(count)
                subD = get_sub_domain(list(subD))
                # print(Hash)
        # print(Hash)
        result = []
        for domain, count in Hash.items():
            result.append("{} {}".format(count, domain))
        return result
