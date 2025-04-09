from collections import Counter


class findMinChanges:
    def findMinChanges(self, currentPassword: str, k:int)-> int:
        n = len(currentPassword)
        groups = []
        res = 0

        for i in range(k // 2):
            group_chars = []
            # Iterate through each segment and collect symmetric pairs (i, k-1-i)
            for j in range(i, n, k):
                if j < n:
                    group_chars.append(currentPassword[j])
                if j + (k - 1 - 2 * i) < n:
                    group_chars.append(currentPassword[j + (k - 1 - 2 * i)])
            groups.append(group_chars)

            # Handle middle positions separately if k is odd
        if k % 2 == 1:
            mid_chars = []
            mid = k // 2
            for j in range(mid, n, k):
                mid_chars.append(currentPassword[j])
            groups.append(mid_chars)

            # Calculate the minimum number of changes
        for group in groups:
            freq_counter = Counter(group)
            most_common_char_freq = max(freq_counter.values())
            # Number of changes = group size minus most frequent character count
            res += len(group) - most_common_char_freq

        return res


