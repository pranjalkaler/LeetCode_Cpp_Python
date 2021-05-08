class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        stack = []
        for x in path:
            if x == ".":
                # do nothing
                pass
            elif x == "..":
                if len(stack) > 0:
                    stack.pop()
            elif x:
                stack.append(x)
        path = ""
        if len(stack) == 0:
            return "/"
        for x in stack:
            path += "/{}".format(x)
        return path