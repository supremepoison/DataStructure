# 双向链表的实现

#　链表节点
class Node:
    def __init__(self, elem):
        self._elem = elem
        self._next = None
        self._prev = None

# 链表类
class DLink:
    # 创建空链表
    def __init__(self):
        self._head = None
    #　判空
    def is_empty(self):
        return self._head == None
    # 遍历显示
    def show(self):
        cur = self._head
        while cur != None:
            print(cur._elem)
            cur = cur._next
    #　插入链表首部
    def add(self, elem):
        #　创建新结点
        tmp = Node(elem)
        if self.is_empty():
            # 空链表
            self._head = tmp
        else:
            # 非空链表
            cur = self._head
            tmp._next = cur
            cur._prev = tmp
            self._head = tmp
    # 删除链表中元素
    def delete(self, data):
        # 三个变量存放遍历时前中后元素结点
        cur, pre = self._head, None
        found = False
        while not found and (cur != None):          
            net = cur._next
            if cur._elem == data:
                found = True
                # 找到数据
                if pre == None:
                    # 该节点是首结点       
                    self._head = net
                    cur._next = None
                    net._prev = None                    
                elif net == None:
                    # 该结点是尾结点
                    cur._prev = None
                    pre._next = None
                else:
                    # 该节点是中间节点
                    pre._next = net
                    net._prev = pre
                    cur._next = None
                    cur._prev = None
            else:
                # 未找到数据
                # 遍历时结点指向
                pre = cur
                cur = cur._next

    # 长度
    def len(self):
        cur, num = self._head, 0
        while cur != None:
            num += 1
            cur = cur._next
        return num


# 自测 
if __name__ == "__main__":
    # 创建自己的链表
    mylink = DLink()
    # 插入数据
    mylink.add('Mary')
    mylink.add('Amy')
    mylink.add('Bob')
    mylink.show()
    print('-'*8)
    # 删除数据
    mylink.delete('Bob')
    mylink.show()
    print('-'*8)
    mylink.delete('Mary')
    mylink.show()
    print('-'*8)
    # 获取长度
    mylink.add('Marco')
    mylink.add('Sofi')
    mylink.delete('Amy')
    mylink.show()
    print('-'*8)
    print(mylink.len())
