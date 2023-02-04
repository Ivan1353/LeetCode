class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int(''.join(map(str, digits)))
        integer += 1
        list2 = list(map(int, list(str(integer))))
        return list2
