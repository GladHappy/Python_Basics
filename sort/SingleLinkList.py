# -*-coding:utf-8
# python_study
# SingleLinkList.py
# @Author: Glad
# @Time: 2020/5/31 15:41

class Node(object):
    """节点,是init，不是int"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None # 初始设置下一节点为空


class SingleLinkList(object):
    """单链表,是init，不是int"""
    def __init__(self, node=None):  # 定义默认参数node,在传入头结点时则接收，在没有传入时，就默认头结点为空
        self.__head = node  # 私有._

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None


    def length(self):  # 不需要参数,除了self之外
        """链表的长度"""
        # cur 游标，用来移动便利节点
        cur = self.__head
        # count记录链表的数量
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur != None:
            print(cur.elem)
            cur = cur.next

    def add(self,item):
        """在链表头添加元素"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """在链表末尾加上元素"""
        node = Node(item)
        # 由于特殊情况当链表为空时没有next，所以在前面要做个判断
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """在指定的位置添加元素"""
        if pos<=0:
            #如果pos在0或者以前，那么当做头插入法来做
            self.add(item)
        elif pos > self.length()-1:
            #如果pos的位置比原链表长，那么当做尾插入法来做
            self.append(item)
        else:
            per = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                per = per.next
            # 当循环退出后，per指向pos-1位置
            node = Node(item)
            node.next = per.next
            per.next = node


    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None
        while cur != None:
            if cur.elem == item:
                #判断是否是头结点
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next


    def search(self, item):
        """查找节点是否存在"""
        cur = self.__head
        while not cur:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())


    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    ll.append(3)
    print(ll.length())

    print('--------1')

    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    print(ll.travel())
    ll.add('Michael')
    print('---------2')
    #print(ll.travel())
    ll.insert(5,'Guan')
    print(ll.travel())
    print('---------3')
    print(ll.remove('Michael'))
    print(ll.remove('Guan'))
    print(ll.remove(3))
    print(ll.remove(5))
    print(ll.travel())
    print('-----------4')
    print(ll.search(5))

