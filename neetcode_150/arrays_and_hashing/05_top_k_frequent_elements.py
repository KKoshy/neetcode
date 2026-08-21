from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # find the count of reach num
        logs = defaultdict(int)
        for num in nums:
            logs[num] += 1

        # create a log with count as the first value to
        # facilitate easy sorting
        count_log = []
        for num, count in logs.items():
            count_log.append([count, num])
        count_log.sort()

        # collect the last k elements (highest frequency)
        results = []
        while len(results) < k:
            results.append(count_log.pop()[1])

        return results


        
        
        
