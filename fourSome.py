import itertools

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sums = []
        for comb in itertools.combinations(nums, 4):
            if sum(comb) == 0 and list(sorted(comb)) not in sums:
                sums.append(list(sorted(comb)))
        return sums