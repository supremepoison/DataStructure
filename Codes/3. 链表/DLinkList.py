# 双向链表的实现

#　链表节点
class Node:
	# 构造函数
	# 通过传入数据值构建链表节点
	# 默认前一链接域为空,none
	# 默认下一链接域为空,none
    def __init__(self, elem):
        self._elem = elem
        self._next = None
        self._prev = None

# 链表类
class DLink:
    # 创建空链表
    def __init__(self):
		# 将链表头部置空,none
        self._head = None

    #　判空
    def is_empty(self):
		# 判断链表头部是否为空即可
        return self._head == None

    # 遍历显示(从前到后遍历)
    def show(self):
		# 获取链表首节点
        cur = self._head
		# 若当前节点为空时结束遍历
        while cur != None:
            print(cur._elem)
			# 将当前节点后移一位
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
			# 备份原链表头部节点
            cur = self._head
			# 新节点的下一链接域指向原链表头部节点cur
            tmp._next = cur
			# 将原链表的头部节点的上一链接域指向新节点
            cur._prev = tmp
			# 更改链表的头部为新节点
            self._head = tmp
    
	# 删除链表中元素
    def delete(self, data):
        # 三个变量存放遍历时前中后元素结点
        cur, pre = self._head, None
		# 定义查找的标志位
        found = False
		# 变量查找
        while not found and (cur != None):  
			# net指向当前的下一链接域
            net = cur._next
			# 找到数据
            if cur._elem == data:
				# 更改标志位found
                found = True
                # 找到数据
                if pre == None:
                    # 该节点是首结点  
					# 更改链表首节点指向要删除数据的下一节点
                    self._head = net
					# 要删除节点的下一链接域置空
                    cur._next = None
					# 新链表首节点的上一链接域置空
                    net._prev = None                    
                elif net == None:
                    # 该结点是尾结点
					# 要删除节点的上一链接域置空
                    cur._prev = None
					# 要删除节点的上一节点,其下一链接域置空
                    pre._next = None
                else:
                    # 该节点是中间节点
					# 将要删除节点的上一节点pre的下一链接域指向要删除节点的下一节点net
                    pre._next = net
					# 将要删除节点的下一节点net的前一链接域指向要删除节点的上一节点pre
                    net._prev = pre
					# 将要删除节点的下一链接域置空
                    cur._next = None
					# 将要删除节点的上一链接域置空
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
    mylink.show() # ->'Bob'  'Amy'  'Mary'
    print('-'*8)
    # 删除数据
    mylink.delete('Bob')
    mylink.show() # -> 'Amy'  'Mary'
    print('-'*8)
    mylink.delete('Mary')
    mylink.show() # -> 'Amy'
    print('-'*8)
    # 获取长度
    mylink.add('Marco')
    mylink.add('Sofi') # -> 'Sofi' 'Marco' 'Amy'
    mylink.delete('Amy') # -> 'Sofi' 'Marco' 
    mylink.show()
    print('-'*8)
    print(mylink.len())# -> 2


C:\Python36\python.exe "C:/Users/Python/Desktop/DataStruc/Codes/3. 链表/DLinkList.py"
Bob
Amy
Mary
--------
Amy
Mary
--------
Amy
--------
Sofi
Marco
--------
2

Process finished with exit code 0
