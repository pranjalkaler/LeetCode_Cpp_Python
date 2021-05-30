class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        merged = []
        N1 = nums1[0:m]
        print(N1)
        front = 0
        while N1 and nums2:
            if N1[front] < nums2[front]:
                merged.append(N1.pop(front))
            else:
                merged.append(nums2.pop(front))
        if not N1:
            merged.extend(nums2)
        else:
            merged.extend(N1)
        # print(merged)
        for i in range(len(merged)):
            # print("merging: {}".format(merged[i]))
            nums1[i] = merged[i]
