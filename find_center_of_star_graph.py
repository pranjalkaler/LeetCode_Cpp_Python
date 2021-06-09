class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        edge_count = []
        for edge in edges:
            if edge[0] in edge_count:
                return edge[0]
            else:
                edge_count.append(edge[0])
            if edge[1] in edge_count:
                return edge[1]
            else:
                edge_count.append(edge[1])
        
#         node_count = 0
#         for edge in edges:
#             node_count += 1
#             edge_count[edge[0]] = edge_count[edge[0]] + 1 if edge[0] in edge_count.keys() else 1
#             edge_count[edge[1]] = edge_count[edge[1]] + 1 if edge[1] in edge_count.keys() else 1
#         print(edge_count, node_count)
#         for x, y in edge_count.items():
#             if y == node_count:
#                 return x
