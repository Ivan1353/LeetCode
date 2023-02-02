from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        deque_ = deque(nums)
        for i in range(k):
            deque_.appendleft(deque_.pop())
        return list(deque_)

        """
        Do not return anything, modify nums in-place instead.
        """

def rotate(nums, k):
    deque_ = deque(nums)
    for i in range (k):
        deque_.appendleft(deque_.pop())
    return list(deque_)