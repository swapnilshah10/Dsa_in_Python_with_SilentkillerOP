class StackUsingQueues:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, data):
        self.queue1.append(data)

    def pop(self):
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        element = self.queue1.pop(0)

        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1

        return element

    def top(self):
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.pop(0))

        element = self.queue1[0]

        # Swap the queues
        self.queue1, self.queue2 = self.queue2, self.queue1

        return element

    def is_empty(self):
        return not bool(self.queue1)

# Example usage
stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.top())  # Output: 3
print(stack.pop())  # Output: 3
print(stack.top())  # Output: 2
