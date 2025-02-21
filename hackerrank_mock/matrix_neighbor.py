from typing import List


class matrix_neighbor:
    def findCircleNum(isConnected: List[str]) -> int:
        # Convert string input into a 2D list of integers
        matrix = [[int(c) for c in row] for row in isConnected]

        def dfs(node: int):
            visited.add(node)
            for neighbor in range(len(matrix)):
                if matrix[node][neighbor] == 1 and neighbor not in visited:
                    dfs(neighbor)

        visited = set()
        groups = 0

        for person in range(len(matrix)):
            if person not in visited:
                groups += 1
                dfs(person)

        return groups
