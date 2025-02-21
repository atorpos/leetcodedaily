from typing import List


class mergearray:

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        mergearray = []
        for i in range(m):
            mergearray.append(nums1[i])
        for i in range(n):
            mergearray.append(nums2[i])
        mergearray.sort()
        for i in range(len(mergearray)):
            nums1[i] = mergearray[i]
