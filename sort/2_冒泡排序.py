# -*-coding:utf-8
# python_study
# 冒泡排序.py
# @Author: Glad
# @Time: 2020/5/17 13:29
# 算法说明
# （1）比较相邻的元素，如果第一个比第二个大，就进行交换；
# （2）对每一对乡里元做同样操作，直到最后一对，最后的元素应该是最大的数；
# （3）循环步骤（1）（2）直到每一任何一对数字需要比较。

def bubble_sort(alist):
    n = len(alist)
    for i in range(0,n-1):
        flag = 0  #标识，用作优化，此时最优时间复杂度为n,就是内层循环的次数.
        for j in range(0,n-1-i):#为什么要减去i，因为当第j个数排序到最后边了，下一轮就不循之前排序好的数据了
            if alist[j]>alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                flag += 1 #如果实现了交换数据的位置，flag就加上1
        if flag ==0: #如果flag等于0，说明序列没有实现数据的交换，则退出
            return alist
    return  alist
if __name__ == '__main__':
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(alist)
    bubble_sort(alist)
    print(alist)