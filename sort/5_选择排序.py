# -*-coding:utf-8
# python_study
# 5_选择排序.py
# @Author: Glad
# @Time: 2020/5/24 22:23

def select_sort(alist):
    """选择排序"""
    n = len(alist)
    for j in range(n-1): #j:0~ n-2
        # j的位置指的是每次比较的起始值，当比较到倒数第二个值的时候(即下标为n-2)，不再往下比较到倒数第1个的值，
        min_index = j
        #有了起始比较值:下标为j，和起始比较值的下标的值应该是j+1,比较最后到最后一个数的值(即下标为:n-1)
        for i in range(j+1,n):
            #当alist[i]的值比alist[min_index]的值小的时候，标记此时值小的数的下标，继续往下循环找比
            #当前标记为min_index的值小的数据，如果有比min_index标记的值小，交换两个值的下标，如果在
            #剩余的数据中没有比min_index标记的值小，此次循环中标记min_index的值最小
            #退出此次当前循环进入下一阶的循环中去。如此反复循环比较数据的大小

            if alist[min_index]>alist[i]:
                min_index = i
        # 交换起始比较值和被比较值的位置后，继续往下寻找比当前的起始比较值
        alist[j],alist[min_index]=alist[min_index],alist[j]

if __name__ =='__main__':
    li = [5,89,1,23,58,46,30,69,47,51,20,3,99,50]
    print(li)
    select_sort(li)
    print(li)