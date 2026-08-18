class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_log = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in num_log:
                length = 0
                while num+length in num_log:
                    length+=1
                longest = max(length, longest)
        return longest
