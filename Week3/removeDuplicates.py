from typing import List

class removeDuplicates:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else :
                nums.remove(num)
        return len(seen)