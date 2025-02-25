from typing import List


class lexicographic02_subarray:

    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7  # To handle large sums
        current_sum = 0  # Rolling prefix sum
        even_count = 1  # Count of even prefix sums (initialize with 1 for empty prefix)
        odd_count = 0  # Count of odd prefix sums
        result = 0  # Total count of sub-arrays with odd sums

        # Traverse the array
        for num in arr:
            current_sum += num  # Update the prefix sum

            # Check if the current prefix sum is even or odd
            if current_sum % 2 == 0:
                result += odd_count  # Add all sub-arrays ending here with odd sum
                even_count += 1  # Increment the count of even prefix sums
            else:
                result += even_count  # Add all sub-arrays ending here with odd sum
                odd_count += 1  # Increment the count of odd prefix sums

            # Take modulus to avoid overflow for large data
            result %= MOD

        return result