from bisect import bisect_left
class countMinOperations:

    def countMinOperations(self, distance, targetDistance):
        distance.sort()
        n = len(distance)

        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + distance[i]

        result = []
        for target in targetDistance:
            idx = bisect_left(distance, target)
            left_sum = idx * target - prefix_sum[idx]
            right_sum = (prefix_sum[n] - prefix_sum[idx]) - (n - idx) * target

            total_operations = left_sum + right_sum
            result.append(total_operations)

        return result
