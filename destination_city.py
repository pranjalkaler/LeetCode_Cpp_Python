class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        def decompose(path, stack):
            sourceNode = [ node for node in stack if node[1] == path[0] ]
            destinationNode = [ node for node in stack if node[0] == path[1] ]
            # print("Source for {} is {}".format(path, sourceNode))
            # print("Destination for {} is {}".format(path, destinationNode))
            
            if sourceNode and destinationNode:
                sourceNode = sourceNode.pop()
                destinationNode = destinationNode.pop()
                stack.remove(sourceNode)
                stack.remove(destinationNode)
                stack.append([sourceNode[0], destinationNode[1]])
            elif sourceNode:
                sourceNode = sourceNode.pop()
                stack.remove(sourceNode)
                stack.append([sourceNode[0], path[1]])
            elif destinationNode:
                destinationNode = destinationNode.pop()
                stack.remove(destinationNode)
                stack.append([path[0], destinationNode[1]])
            else:
                stack.append(path)

        stack = []
        while paths:
            path = paths.pop(0)
            decompose(path, stack)
            # print(stack)
        return stack[0][1]
