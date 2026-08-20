class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        logs = {}
        for i in range(len(nums)):
            if target - nums[i] in logs:
                return [logs[target - nums[i]], i] 
            else:
                logs[nums[i]] = i
    
