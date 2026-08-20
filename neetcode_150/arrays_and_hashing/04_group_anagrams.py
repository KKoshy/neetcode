from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list)
        for word in strs:
            log = [0] * 26
            for char in word:
                log[ord(char) - ord('a')] += 1
            results[tuple(log)].append(word)
        return list(results.values())
        
