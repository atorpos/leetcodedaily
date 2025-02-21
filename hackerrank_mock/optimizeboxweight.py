from typing import List


class optimizeboxweight:
    def minimalHeaviestSetA(arr: List[int]) -> List[int]:
        sumofsubset = 0
        arr.sort()
        maxsum = arr[0] + arr[1]
        for i in range(1, len(arr)):
            sumofsubset = sumofsubset + arr[i]

        if maxsum > sumofsubset:
            return [arr[1], arr[0]]



