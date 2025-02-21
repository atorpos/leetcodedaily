from typing import List


class twosum:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        accept_value = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    print(nums[i], nums[j])
                    accept_value = [i, j]
        return accept_value