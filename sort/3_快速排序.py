# -*-coding:utf-8
# python_study
# 3_快速排序.py
# @Author: Glad
# 列表中所有的值选左边第一个值做中间值，标记左边第二个为low，列表最右边的值标记为high
# 从high标记的值和中间值做比较，如果high的值比中间值大或者等于中间值，high标记自动减1，当high标记的值比中间值小的时候，把值换到low标记的位置上(因为此时low的值赋值给mid_value)
# ，比较low的值和中间值的大小.如果low的值小于中间值，low自动加1，当low标记的值大于中间值的时候，把low标识的值换到标记为high的位置上，如此交替和中间值比较大小，当low标记的位置和high标记
# 的位置是同一个位置时候，表明第一次标记的中间值找到了它在这个列表中的真正位置，此时标记为alist[low]=mid_value。列表中在中间值左边的是小于中间值的数据，在中间值右边的是大于中间值的数据，
# 把小于中间值的数据看作一个整体再继续按照刚才排序的方法排序;在中间值右边的数据也看作一个整体继续按照刚才的方法做排序。当列表中分出的部分只有1个值的时候(即low的值等于high的值时候)
# 不可再分，循环就结束.在这个排序中小于中间值的数据和大于中间值的数据套用第一次做排序的方法，这个方法叫递归.
# @Time: 2020/5/23 22:52

def quick_sort(alist,first,last):
    """快速排序"""
    # 如果下标first>=last时候，就意味着列表中要排序值个数=1，就返回
    if first >= last:
        return
    mid_value = alist[first]
    low = first
    high = last
    while low < high:
        # hight 左移动,如果遇到的值等于设定的中间值，继续左移动,如果值等于中间值，都放在右边
        while low < high and alist[high] >= mid_value:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    #从上面的循环退出的时候，即 low == high
    alist[low] = mid_value

    #对low左边的列表执行快速排序
    quick_sort(alist,first,low-1)

    # 对low右边的列表执行快速排序
    quick_sort(alist,low+1,last)


if __name__ == '__main__':
    li = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(li)
    quick_sort(li,0,len(li)-1)
    print(li)
