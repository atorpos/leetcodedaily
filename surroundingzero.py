from typing import List


class surrandingzero:

    def surround_with_zero(self, grid: List[List[str]]) -> int:
        no_of_islane = 0

        row, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= row or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(row):
            for c in range(cols):
                if grid[r][c] == '1':
                    no_of_islane +=1
                    dfs(r, c)

        return no_of_islane

    def reorderLogFile(self, logs: List[str]) -> List[str]:
        new_list: List[str] = []
        dig_list: List[str] = []
        let_list: List[str] = []
        for contain_item in logs:
            iddentifier, content = contain_item.split(" ", 1)
            if content[0].isdigit():
                dig_list.append(contain_item)
            else:
                let_list.append(contain_item)
        let_sort_list = sorted(let_list, key=lambda x: (x.split(" ", 1)[1], x.split(" ", 1)[0]))
        new_list.extend(let_sort_list)
        new_list.extend(dig_list)
        return new_list

    def numberOfWays(self, s: str) -> int:
        n = len(s)
        no_of_way = 0

        for k in range(n):
            for i in range(k+1, n):
                if s[i] != s[k]:
                    for j in range(i+1, n):
                        if s[j] != s[i]:
                            no_of_way += 1

        return no_of_way

    def maxmumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = []
        curr_sum = 0
        for i in range(len(nums)-k + 1):
            subarray = nums[i:i+k]
            if len(subarray) != len(set(subarray)):
                continue
            curr_sum = sum(nums[i:i+k])
            max_sum.append(curr_sum)
        if len(max_sum) == 0:
            return 0
        return max(max_sum)

    def kthKactor(self, n: int, k: int) -> int:
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        if len(divisors) < k:
            return -1
        return divisors[k-1]

    def partitionString(self, s: str) -> int:
        seen = set()
        partition_array = []
        segment = ""
        for char in s:
            if char in seen:
                partition_array.append(segment)  # Save the current segment
                segment = ""  # Start a new segment
                seen.clear()  # Reset the seen set
            segment += char  # Add the character to the current segment
            seen.add(char)  # Mark it as seen
        if segment:
            partition_array.append(segment)

        return len(partition_array)

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        sentence_array = paragraph.lower().split()

        return sentence_array[0]




