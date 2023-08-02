#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#
import heapq
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(nums1)):
            heapq.heappush(pq, [nums1[i], nums2[0], 0])
        heapq.heapify(pq)
        res = []
        while pq and k > 0:
            n1, n2, i = heapq.heappop(pq)
            if i + 1 < len(nums2):
                heapq.heappush(pq, [n1, nums2[i + 1], i + 1])
            res.append([n1, n2])
            k -= 1
        return res

# @lc code=end

