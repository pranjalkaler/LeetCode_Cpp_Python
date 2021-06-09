class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def inOrder(node, children):
            child_list = []
            main_list = []
            
            for child in children:
                child_list = inOrder(child, graph[child])
                for x in child_list:
                    main_list.append("{}|{}".format(node, x))
            # print("Main list at {} = {}".format(node, main_list))
            return main_list if main_list else [ "{}".format(node) ]
        result = []
        destinations = inOrder(0, graph[0])
        for dest in destinations:
            dest = [int(x) for x in dest.split('|')]
            final_destination = []
            for x in dest:
                final_destination.append(x)
                if x == n-1:
                    break

            if final_destination[-1] == n - 1:
                result.append(final_destination)

        return result
