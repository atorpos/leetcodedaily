class findMinimumTime:
    def findMinimumTime(self, password, attackOrder, m):
        length = len(password)

        # Helper function to identify if a given number of attacks leads to required infected substrings
        def check_infected(attempts):
            infected = [False] * length

            # Mark attacked positions as infected
            for idx in range(attempts):
                infected[attackOrder[idx] - 1] = True  # positions start from 1, adjust to 0-based

            total_substrings = length * (length + 1) // 2
            clean_substrings = count_clean_substrings(infected)
            infected_substrings = total_substrings - clean_substrings

            # Check if we have at least the required number of infected substrings
            return infected_substrings >= m

        # Function to calculate substrings with no infected positions
        def count_clean_substrings(infected_positions):
            count = 0
            idx = 0
            while idx < length:
                if not infected_positions[idx]:
                    end = idx
                    while end < length and not infected_positions[end]:
                        end += 1
                    clean_length = end - idx
                    count += clean_length * (clean_length + 1) // 2
                    idx = end
                else:
                    idx += 1
            return count

        # Binary search to find minimum required attacks
        left, right = 1, length
        answer = length
        while left <= right:
            mid = (left + right) // 2
            if check_infected(mid):
                answer = mid
                right = mid - 1  # Might find a smaller answer, search left
            else:
                left = mid + 1  # Need more attacks, search right

        return answer


