# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 215 数组中的第K个最大元素
# @Content : 在未排序的数组中找到第 k 个最大的元素。
#            请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
from typing import List
import heapq as hq  # 可借助python中的heapq模块实现堆的功能, 注意建立的是小根堆


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            hq.heappush(heap, i)
            if len(heap) > k:
                hq.heappop(heap)
        return heap[0]

class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = nums[:k]
        # 建立含k个元素的小根堆
        for i in range((k-2)//2, -1, -1):
            self.sift(heap, i, k-1)

        # 若k之后的元素大于根节点，则将该元素与根节点替换，然后做一次调整
        for j in range(k, n):
            if nums[j] > heap[0]:  # 找前k大的数
                heap[0] = nums[j]
                self.sift(heap, 0, k-1)
        # print(heap)
        return heap[0]  # 堆顶就是第k大的数了

    # 注意这里要建立小根堆
    def sift(self, alist, low, high):
        # 假设只有根节点需要调整，两棵子树都是堆
        i = low
        j = i *2 +1 #j指向i的左子树
        tmp = alist[i]
        while j <= high:
            if j+1 <= high and alist[j] > alist[j+1]: #右子树比较小,则指向右子树
                j = j+1
            if alist[j] < tmp:  # 若子树的值比较小，则根节点换成子树，然后向下看一层
                alist[i] = alist[j]
                i = j
                j = i *2 +1
            else:
                alist[i] = tmp # 子树的值大于根节点，则根节点就放在这一层
                break
        else:
            alist[i] = tmp # j越界跳出循环，则把根节点放在叶子节点


if __name__ == '__main__':
    # case1  res = 5
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2

    # case2  res = 4
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4

    sol = Solution()
    res1 = sol.findKthLargest(nums1, k1)
    res2 = sol.findKthLargest(nums2, k2)
    print('case1:', res1)
    print('case2:', res2)