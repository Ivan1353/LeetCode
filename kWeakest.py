import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        reducedList = list(map(sum, mat))
        return heapq.nsmallest(k, range(len(reducedList)), key=reducedList.__getitem__)
