from typing import List


class maxSubset:

    def optimize_box_weight(arr: List[int]):
        # Sort the array in descending order
        arr.sort(reverse=True)

        A = []  # Subset A
        sum_A = 0
        total_sum = sum(arr)  # Total weight of all elements

        # Iterate through the array to construct subset `A`
        for weight in arr:
            A.append(weight)  # Add current element to A
            sum_A += weight  # Update sum of A

            # Check if Sum(A) > Sum(B)
            if sum_A > (total_sum - sum_A):  # If Sum(A) > Sum(B)
                # As soon as the condition is satisfied, break the loop
                break

        # Sort A in ascending order before returning
        A.sort()
        return A
