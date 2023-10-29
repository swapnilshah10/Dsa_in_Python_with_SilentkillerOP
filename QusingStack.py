class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack1.append(data)
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if not self.stack1:
            return None
        return self.stack1.pop()

    def front(self):
        if not self.stack1:
            return None
        return self.stack1[-1]

    def is_empty(self):
        return not bool(self.stack1)

# Example usage
queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.front())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.front())  # Output: 2
