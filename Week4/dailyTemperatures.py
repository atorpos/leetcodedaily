from typing import List


class dailyTemperatures:

    def dailytemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]* len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                statkT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([temp, i])

        return res