from typing import List


class lexicographic01:

    def lexicalOrder(self, n: int) -> List[int]:
        array_nos = []
        for i in range(1, n+1):
            array_nos.append(i)
            print(i)
        return sorted(array_nos, key=str)