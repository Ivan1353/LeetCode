class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        for item in dict1.items():
            if item[1] == 1:
                return item[0]
