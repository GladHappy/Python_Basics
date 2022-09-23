# -*-coding:utf-8
# python_study
# 1_希尔排序.py
# @Author: Glad
# @Time: 2020/5/17 1:04

def shell_sort(alist):
    n = len(alist) #列表的长度
    gap =  n // 2   #步长 （这个步长不一定最优）

    #gap变化到0之前，插入算法的执行次数
    while gap>0:
        #起始值从gap的开始，到列表的长度n结束
        #希尔排序与普通的插入排序不同点是gap的长度
        for j in range(gap,n):
            #j = [gap+1,gap+2,gap+3 ....n-1]
            i = j
            while i>0:  #下标元素到0截止
                #如果当前元素比前一个元素的值小，交换俩个数的位置
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap]=alist[i-gap],alist[i]
                    #下标的值往前挪动，减去一个步长的值
                    i -= gap
                else:
                    break
        #当前的步长循环结束后，缩短当前的步长
        gap//=2


if __name__ == '__main__':
    alist = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(alist)
    shell_sort(alist)
    print(alist)

    # 稳定性： 不稳定
    # 时间复杂度：跟步长有关