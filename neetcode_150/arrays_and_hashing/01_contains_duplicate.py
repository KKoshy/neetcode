class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        other = []
        for num in nums:
            if num in other:
                return True
            other.append(num)
        return False
