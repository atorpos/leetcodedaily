from typing import List


class minimumAbsoluteDifference:
    def minimumabsolutedifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = min(abs(arr[i] - arr[i - 1]) for i in range(1, len(arr)))

        result = []
        for i in range(0, len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == min_diff:
                result.append([arr[i], arr[i + 1]])
        return result
