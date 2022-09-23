# -*-coding:utf-8
# python_study
# 4_插入排序.py
# @Author: Glad
# @Time: 2020/5/24 16:54

def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    flag = 0
    for j in range(1,n):
        # i表示内层循环起始值
        i = j
        while i>0:
            if alist[i]<alist[i-1]:
                alist[i],alist[i-1]=alist[i-1],alist[i]
                i -= 1
                flag += 1
            # 插入排序排序好的数据是顺序的，如果比i的值大，肯定比i-1的值大，所以就退出.
            else:
                break
    print(flag)



if __name__=='__main__':
    alist=[12,11,10,9, 8, 7, 6, 5, 4, 3, 2, 1]
    #alist = [78, 21, 1, 5, 98, 100, 3586, 18, 63, 98, 52, 10, 72, 15, 46, 32, 58, 44]
    print(alist)
    insert_sort(alist)
    print(alist)
