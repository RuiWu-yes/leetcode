# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 215 数组中的第K个最大元素
# @Content : 在未排序的数组中找到第 k 个最大的元素。
#            请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
from typing import List
import heapq as hq  # 可借助python中的heapq模块实现堆的功能, 注意建立的是小根堆
import random


class Solution1:
    # 暴力法(全局排序后取倒数第k个数)
    # 时间复杂度O(NlogN)，空间复杂度O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        nums.sort()
        return nums[size - k]


class Solution2:
    # 利用heapq实现堆
    # 思路：维护一个大小为k的最小堆，堆顶是这k个数里的最小的，遍历完数组后返回堆顶元素即可
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for i in nums:
            hq.heappush(heap, i)
            if len(heap) > k:
                hq.heappop(heap)
        return heap[0]


class Solution3:
    # 自己实现堆
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heap = nums[:k]
        # 建立含k个元素的小根堆
        for i in range((k-2) // 2, -1, -1):
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
        j = i * 2 + 1  # j 指向i的左子树
        tmp = alist[i]
        while j <= high:
            if j+1 <= high and alist[j] > alist[j+1]:  # 右子树比较小,则指向右子树
                j = j + 1
            if alist[j] < tmp:  # 若子树的值比较小，则根节点换成子树，然后向下看一层
                alist[i] = alist[j]
                i = j
                j = i * 2 + 1
            else:
                alist[i] = tmp  # 子树的值大于根节点，则根节点就放在这一层
                break
        else:
            alist[i] = tmp  # j 越界跳出循环，则把根节点放在叶子节点


class Solution4:
    # 借助 partition 操作定位到最终排定以后索引为 len - k 的那个元素（特别注意：随机化切分元素）
    # 时间复杂度O(N)，空间复杂度O(1)

    # 注意：本题必须随机初始化 pivot 元素，否则通过时间会很慢，因为测试用例中有极端测试用例。
    # 说明：最极端的是顺序数组与倒序数组，此时递归树画出来是链表，时间复杂度是 O(N^2)，根本达不到减治的效果。
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        target = size - k
        left, right = 0, size - 1
        while True:
            # index = self.__partition1(nums, left, right)   # 减治法，“只要”递归一个分支
            # index = self.__partition2(nums, left, right)
            index = self.__partition3(nums, left, right)
            if index == target:
                return nums[index]
            elif index < target:
                # 下一轮在 [index + 1, right] 里找
                left = index + 1
            else:
                right = index - 1

    #  循环不变量：[left + 1, j] < pivot
    #  (j, i) >= pivot
    def __partition1(self, nums, left, right):
        # 方法一：直接使用最左边的值作为pivot，极端情况表现不佳
        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    def __partition2(self, nums, left, right):
        # 方法二：为了应对极端测试用例，使得递归树加深，可以在循环一开始的时候，随机交换第 1 个元素与它后面的任意 1 个元素的位置
        # 随机化切分元素
        random_index = random.randint(left, right)  # randint 是包括左右区间的
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]
        j = left
        for i in range(left + 1, right + 1):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        return j

    # 循环不变量：
    # [left + 1, lt） <= pivot
    # (rt, right] >= pivot
    def __partition3(self, nums, left, right):
        # 方法三：使用双指针，将与 pivot 相等的元素等概论地分到 pivot 最终排定位置的两边。
        # randint 是包括左右区间的
        random_index = random.randint(left, right)
        nums[random_index], nums[left] = nums[left], nums[random_index]

        pivot = nums[left]

        lt = left + 1
        rt = right

        while True:
            while lt <= rt and nums[lt] < pivot:
                lt += 1
            while lt <= rt and nums[rt] > pivot:
                rt -= 1

            if lt > rt:
                break
            nums[lt], nums[rt] = nums[rt], nums[lt]
            lt += 1
            rt -= 1

        nums[left], nums[rt] = nums[rt], nums[left]
        return rt


class Solution5:
    def findKthLargest(self, nums: List[int], k: int):
        # 二分法
        # 使用一个长度为k的小数组存储前k个元素（大小）；
        # 遍历数组，使用二分法查找小数组中第一个比当前元素小的数
        res = [float('-inf') for _ in range(k)]
        for n in nums:
            # 如果当前元素小于等于数组中最小的元素
            if n <= res[0]:
                continue
            # 如果当前元素大于等于数组中最大的元素
            if n >= res[-1]:
                res = res[1:] + [n]
                continue

            # 二分法定位要插入的位置
            left = 0
            right = k - 1
            while left < right:
                mid = (left + right) // 2

                # 如果i <= res[mid]，则需要插入的位置一定在mid的左边，不包括mid
                if n <= res[mid]:
                    right = mid - 1
                # 如果i > res[mid]并且i小于mid的下一个元素，则插入的位置在mid
                elif res[mid + 1] >= n:
                    left = mid
                    break
                # 插入的位置在mid之后，不包括mid
                else:
                    left = mid + 1
            # 新的前k元素数组
            res = res[1:left + 1] + [n] + res[left + 1:]
        return res[0]


if __name__ == '__main__':
    # case1  res = 5
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2

    # case2  res = 4
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4

    sol1, sol2, sol3, sol4, sol5 = Solution1(), Solution2(), Solution3(), Solution4(), Solution5()
    res1 = sol1.findKthLargest(nums1, k1), sol2.findKthLargest(nums1, k1),\
           sol3.findKthLargest(nums1, k1), sol4.findKthLargest(nums1, k1), sol5.findKthLargest(nums1, k1)
    res2 = sol1.findKthLargest(nums2, k2), sol2.findKthLargest(nums2, k2),\
           sol3.findKthLargest(nums2, k2), sol4.findKthLargest(nums2, k2), sol5.findKthLargest(nums2, k2)
    print('case1:', res1)
    print('case2:', res2)