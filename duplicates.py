class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        reduced_nums = list(set(nums))
        underscore_number = len(nums)-len(reduced_nums)
        length= len(reduced_nums)
        for i in range (underscore_number):
            reduced_nums.append("_")
        return f"{length}, nums = {reduced_nums}"