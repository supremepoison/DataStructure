# 基于链式存储的栈结构


# 自定义节点结构
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# 链式栈
class LStack:
    # 构建空栈　－　空节点
    def __init__(self):
        self._head = Node()
        self._count = 0

    # 判空
    def is_empty(self):
        return self._count == 0

    #　判满　(因使用链式结构来实现无固定大小，故不需要判满)

    #　压入数据  
    def push(self, elem): # 100 
        # 通过传入数据elem创建数据节点
        tmp = Node(elem) # Node(100)
        # 新节点放人栈中
        if self.is_empty():
			# 当为空栈的时候
			# 直接将栈顶指向新数据节点即可
            self._head = tmp
        else:
			# 当非空栈时
			# 将新数据节点的下一链接域执行原栈顶
            tmp.next = self._head
			# 变更栈顶位置,指向新数据节点
            self._head = tmp
        #　栈中数据节点计数加一
        self._count += 1

    # 弹出数据
    def pop(self):
        # 需要判断栈是否为空
        if self.is_empty():
            raise IndexError("stack error:试图从空栈中弹出数据")
        else:
            # 节点数目减一
            self._count -= 1
            # 保存原栈顶节点数据
            tmp = self._head
            # 栈顶变更
            self._head = self._head.next
            # 将原栈顶节点的下一链接域置为空
            tmp.next = None
            # 返回数据
            return tmp.data


# 自测代码
if __name__ == "__main__":
    # 创建自己的栈
    mystack = LStack()
    #　压入数据 10/20/30/40
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.push(40)
    # 弹出所有数据
    while not mystack.is_empty():
        print(mystack.pop())
    #　试图从空栈中弹出数据
    mystack.pop()
