# 单向链表的实现

#　链表节点
class Node:
	# 构造函数
	# 通过传入数据构造新节点
	# 默认下一链接域为空,none
    def __init__(self, elem):
        self._elem = elem
        self._next = None

# 链表类
class SLink:
    # 创建空链表
	# 将链表头置为空,none
    def __init__(self):
        self._head = None
    
	#　判空
    def is_empty(self):
		# 根据初始化判断链表头是否为空即可
        return self._head == None
    
	# 遍历显示
    def show(self):
		# 获取第一个链表节点
        cur = self._head
		# 若节点为空时结束遍历
        while cur != None:
            print(cur._elem)
			# 将当前的节点后移一位
            cur = cur._next

    #　插入链表首部
    def add(self, elem):
        #　创建新结点
        tmp = Node(elem)
        # 新结点插入首部
        tmp._next = self._head
        # 更改链表首结点
        self._head = tmp

    # 删除链表中元素
    def delete(self, data):
        # 两个变量存放遍历时前后两个元素结点
        cur, pre = self._head, None
		# 查找标志位found
        found = False
        while not found and (cur != None):          
            if cur._elem == data:
                # 找到数据
				# 更改标志位found
                found = True
                if pre == None:
                    # 该节点是首结点
					# 更改链表头部,指向第二个节点
                    self._head = cur._next
					# 将要删除节点的下一链接域置空
                    cur._next = None
                else:
                    # 该节点是中间节点或尾结点
					# 将前一节点的下一链接域指向当前节点的下一节点
                    pre._next = cur._next
					# 将要删除节点的下一链接域置空
                    cur._next = None

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
    mylink = SLink()
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


#C:\Python36\python.exe "C:/Users/Python/Desktop/DataStruc/Codes/3. 链表/SLinkList.py"
#Bob
#Amy
#Mary
#--------
#Amy
#Mary
#--------
#Amy
#--------
#Sofi
#Marco
#--------
#2
#
#Process finished with exit code 0
