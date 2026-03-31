class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        merged_intervals = [intervals[0]]
        for current_start, current_end in intervals[1:]:
            last_merged_start, last_merged_end = merged_intervals[-1]
            if current_start <= last_merged_end:
                merged_intervals[-1][1] = max(last_merged_end, current_end)
            else:
                merged_intervals.append([current_start, current_end])
        return merged_intervals




        