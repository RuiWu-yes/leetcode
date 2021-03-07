# -*- coding: utf-8 -*-
# @Author  : ruiwu
# @Email   : ryanwoo@zju.edu.cn
# @Title   : 155 最小栈
# @Content : 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。
#               push(x) —— 将元素 x 推入栈中。
#               pop() —— 删除栈顶的元素。
#               top() —— 获取栈顶元素。
#               getMin() —— 检索栈中的最小元素。
#      提示 ： pop、top 和 getMin 操作总是在 非空栈 上调用。


class MinStack1:
    # 辅助栈和数据栈同步
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []  # 数据栈
        self.helper = []  # 辅助栈

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])  # 同步添加（保证辅助栈栈顶位为最小值）

    def pop(self) -> None:
        if self.data:
            # 同步删除data、helper栈顶元素
            self.helper.pop()
            return self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]


class MinStack2:
    # 辅助栈和数据栈不同步
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []  # 数据栈
        self.helper = []  # 辅助栈

    def push(self, x: int) -> None:
        self.data.append(x)
        # 关键1：辅助栈的元素空的时候，必须放入新进来的数
        # 关键2：新来的数小于或者等于辅助栈栈顶元素的时候，才放入（特别注意这里等于要考虑进来）
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        # 关键3：出栈的时候，辅助栈的栈顶元素等于数据栈的栈顶元素，才出栈，即“出栈保持同步”就可以了
        #    注：不论怎么样，数据栈都要pop出元素
        top = self.data.pop()
        if self.helper and top == self.helper[-1]:
            self.helper.pop()
        return top

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]