class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = list()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.l.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        val = self.l[len(self.l)-1]
        del self.l[len(self.l)-1]
        return val

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.l[len(self.l)-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if(len(self.l) == 0):
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()