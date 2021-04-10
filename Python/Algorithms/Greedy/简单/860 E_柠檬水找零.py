# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 860 柠檬水找零
# @Content : 在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
#            顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
#            每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，
#            也就是说净交易是每位顾客向你支付 5 美元。
#            注意，一开始你手头没有任何零钱。
#            如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 贪心算法
        # 局部最优：遇到账单20，优先消耗美元10，完成本次找零。
        # 全局最优：完成全部账单的找零。
        # 只需要维护三种金额的数量，5，10和20。
        # 有如下三种情况：
        #    情况一：账单是5，直接收下。
        #    情况二：账单是10，消耗一个5，增加一个10
        #    情况三：账单是20，优先消耗一个10和一个5，如果不够，再消耗三个5
        # 此时大家就发现 情况一，情况二，都是固定策略，都不用我们来做分析了，而唯一不确定的其实在情况三。
        # 而情况三逻辑也不复杂甚至感觉纯模拟就可以了，其实情况三这里是有贪心的。
        # 账单是20的情况，为什么要优先消耗一个10和一个5呢？
        #    因为美元10只能给账单20找零，而美元5可以给账单10和账单20找零，美元5更万能！
        five = ten = 0
        # twenty = 0
        for bill in bills:
            # 情况一
            if bill == 5: five += 1
            # 情况二
            if bill == 10:
                if five <= 0: return False
                ten += 1
                five -= 1
            # 情况三
            if bill == 20:
                # 优先消耗10美元，因为5美元的找零用处更大，能多留着就多留着
                if five > 0 and ten > 0:
                    five -= 1
                    ten -= 1
                    # twenty += 1  # 其实这行代码可以删了，因为记录20已经没有意义了，不会用20来找零
                elif five >= 3:
                    five -= 3
                    # twenty += 1  # 同理，这行代码也可以删了
                else:
                    return False
        return True


if __name__ == '__main__':
    # case1  res = true
    # 解释：
    # 前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
    # 第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
    # 第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
    # 由于所有客户都得到了正确的找零，所以我们输出 true。
    bills1 = [5, 5, 5, 10, 20]

    # case2  res = true
    bills2 = [5, 5, 10]

    # case3  res = false
    bills3 = [10, 10]

    # case4  res = false
    # 解释：
    # 前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
    # 对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
    # 对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
    # 由于不是每位顾客都得到了正确的找零，所以答案是 false。
    bills4 = [5, 5, 10, 10, 20]

    sol = Solution()
    res1 = sol.lemonadeChange(bills1)
    res2 = sol.lemonadeChange(bills2)
    res3 = sol.lemonadeChange(bills3)
    res4 = sol.lemonadeChange(bills4)
    print('case1:', res1)
    print('case2:', res2)
    print('case3:', res3)
    print('case4:', res4)