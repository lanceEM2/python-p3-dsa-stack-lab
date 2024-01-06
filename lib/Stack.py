class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if (len(self.items) <= self.limit):
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            return "Stack overflow limit exceeded"

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if (len(self.items) >= self.limit):
            return True
        else:
            return False

    def search(self, target):
        # start, stop, step
        for i in range(len(self.items) -1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - i - 1
        return -1
