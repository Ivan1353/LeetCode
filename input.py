class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        while val in nums:
            nums.remove(val)
            counter += 1
        for i in range (counter):
            nums.append("_")
        return nums