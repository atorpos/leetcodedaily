from typing import List


class solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

    def merge_intervals(self, time_ranges: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort the time ranges based on the start time
        time_ranges.sort(key=lambda time_range: time_range[0])

        # List to store the merged time intervals
        merged_ranges = []

        for current_range in time_ranges:
            # If no ranges in merged_ranges yet or no overlap with the last merged range
            if not merged_ranges or merged_ranges[-1][1] < current_range[0]:
                merged_ranges.append(current_range)
            else:
                # There is an overlap, so merge by updating the end time of the last merged range
                merged_ranges[-1][1] = max(merged_ranges[-1][1], current_range[1])

        return merged_ranges
