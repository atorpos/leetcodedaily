from typing import List

class longestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            print(f"the first loop, {strs[0][:i]}")
            for j in range(1, len(strs)):
                if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]