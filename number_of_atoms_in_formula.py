class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        formula = list(formula)
        while formula:
            if formula[0] == "(":
                stack.append(["(", 1])
                formula.pop(0)
            elif formula[0].isupper():
                element = formula.pop(0)
                if len(formula) >= 1 and formula[0].islower():
                    # double lettered element
                    element += formula.pop(0)
                stack.append([element, 1])
            elif formula[0].isnumeric():
                number = int(formula.pop(0))
                while formula and formula[0].isnumeric():
                    number = number*10 + int(formula.pop(0))
                stack[-1][1] = number
            elif formula[0] == ")":
                formula.pop(0)
                if formula and formula[0].isnumeric():
                    number = int(formula.pop(0))
                    while formula and formula[0].isnumeric():
                        number = number*10 + int(formula.pop(0))
                else:
                    number = 1
                tempStack = []
                while stack[-1][0] != "(":
                    tempStack.append(stack.pop())
                stack.pop()
                while tempStack:
                    elem = tempStack.pop()
                    elem = [elem[0], number*elem[1]]
                    stack.append(elem)
        print(stack)
        dictionary = {}
        for x in stack:
            if x[0] in dictionary.keys():
                dictionary[x[0]] += x[1]
            else:
                dictionary[x[0]] = x[1]
        print(dictionary)
        dictionary1 = {x: dictionary[x] for x in sorted(dictionary.keys())}
        print(dictionary1)
        result = ""
        for elem, count in dictionary1.items():
            if count > 1:
                result += "{}{}".format(elem, count)
            else:
                result += elem
        return result
            
                
            