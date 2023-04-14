class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.l.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        val = self.l[0]
        del self.l[0]
        return val

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.l[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if(len(self.l) == 0):
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()