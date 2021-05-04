# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    
    def getFlatList(self, val):
        finalList = []
        for x in val:
            if type(x) == NestedInteger:
                if x.isInteger():
                    finalList.append(x.getInteger())
                else:
                    finalList.extend(self.getFlatList(x.getList()))
        # print(finalList)
        return finalList
    
    def __init__(self, nestedList: [NestedInteger]):
        self.mainList = self.getFlatList(nestedList)
        self.itr = 0
        # print("MAINLIST: {}".format(self.mainList))
        
    def next(self) -> int:
        self.itr += 1
        return self.mainList[self.itr - 1]

    def hasNext(self) -> bool:
        return True if self.itr < len(self.mainList) else False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())