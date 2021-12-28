# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.array = list()
        while iterator.hasNext():
            self.array.append(iterator.next())
        # print(self.array)
        self.pos = -1
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.array[self.pos + 1]

    def next(self):
        """
        :rtype: int
        """
        self.pos = self.pos + 1
        return self.array[self.pos]

    def hasNext(self):
        """
        :rtype: bool
        """
        # print("pos = ", self.pos)
        return len(self.array) > 0 and self.pos < len(self.array) - 1
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].