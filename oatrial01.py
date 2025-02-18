from typing import List

class oatrial:
    def get_key_identifier(key: str) -> str:
        # Frequency count of each character
        from collections import Counter
        freq = Counter(key)

        # Separate characters into half palindrome and the middle character (if odd frequency exists).
        half_palindrome = []  # First half of the palindrome
        middle_char = ''  # Odd frequency character, if any

        for char in sorted(freq.keys()):  # Process characters in lexicographical order
            count = freq[char]
            if count % 2 == 1:
                middle_char = char  # Use the odd-frequency character as the middle one
            half_palindrome.append(char * (count // 2))  # Append half the count of each character

        # Join the half palindrome and middle character, and mirror it to create the full palindrome
        half_palindrome = ''.join(half_palindrome)
        return half_palindrome + middle_char + half_palindrome[::-1]

    def calculate_min_total_wattage(bulb_wattages: List[int], num_to_remove: int) -> int:
        # Total wattage of all bulbs
        total_wattage = sum(bulb_wattages)

        # Edge case: If num_to_remove is 0, no bulbs are removed
        if num_to_remove == 0:
            return total_wattage

        # Find the maximum wattage of any contiguous subarray of length num_to_remove
        n = len(bulb_wattages)
        k = num_to_remove

        # Sliding window to find max wattage subarray of size k
        max_wattage_removed = 0
        current_window_sum = sum(bulb_wattages[:k])
        max_wattage_removed = current_window_sum

        for i in range(k, n):
            # Slide the window by adding the next element and removing the previous one
            current_window_sum += bulb_wattages[i] - bulb_wattages[i - k]
            max_wattage_removed = max(max_wattage_removed, current_window_sum)

        # Answer is the total wattage minus the max wattage of removed bulbs
        return total_wattage - max_wattage_removed

    def get_maximum_greyness(pixels: List[str]) -> int:
        n = len(pixels)  # Number of rows
        m = len(pixels[0])  # Number of columns

        # Precompute the number of 1's in each row and column
        row_ones = [sum(int(cell) for cell in row) for row in pixels]
        col_ones = [sum(int(pixels[i][j]) for i in range(n)) for j in range(m)]

        max_greyness = float('-inf')  # Initialize max greyness to a very small value

        # Calculate greyness for each cell
        for i in range(n):
            for j in range(m):
                greyness = 2 * (row_ones[i] + col_ones[j]) - n - m
                max_greyness = max(max_greyness, greyness)

        return max_greyness
