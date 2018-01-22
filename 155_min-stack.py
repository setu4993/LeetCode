class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minimum = 2147483648

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        self.minimum = min(self.minimum, x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if self.stack:
            if x == self.minimum:
                self.minimum = min(self.stack)
        else:
            self.minimum = 2147483648
        return x

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minimum

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
#obj.push(2)
#obj.push(-2)
#obj.push(3)
#obj.push(0)
#print(obj.pop())
#print(obj.top())
# obj.pop()
# print(obj.getMin())

commands = ["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
values = [[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
for c, v in zip(commands, values):
    print(c)
    if c == "push":
        obj.push(v[0])
    elif c == "getMin":
        print(obj.getMin())
    elif c == "top":
        print(obj.top())
    elif c == "pop":
        print(obj.pop())