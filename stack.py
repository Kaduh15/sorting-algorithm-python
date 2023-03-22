class Stack:
    def __init__(self):
        self._stack = []

    def add(self, item):
        self._stack.append(item)

    def isEmpty(self):
        return not self._stack

    def pop(self):
        if self.isEmpty():
            return None
        return self._stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def __len__(self):
        return self.size()

    def __str__(self):
        returnString = ""
        for el in self._stack:
            returnString += f"{el} "
        return returnString
