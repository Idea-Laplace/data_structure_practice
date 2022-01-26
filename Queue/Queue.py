class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.size = 0
        self.end = None

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    def enqueue(self, element):
        temp = Node(element)
        if self.end:
            temp.next = self.end
        self.end = temp
        self.size += 1

    def dequeue(self):
        if not self.end:
            raise IndexError
        value = self.end.data
        self.end = self.end.next
        self.size -= 1
        return value

    def __repr__(self):
        expr = ' >> EXIT'
        content = self.end
        while content:
            expr = f' >> {content.data}' + expr
            content = content.next
        expr = 'ENTRANCE' + expr
        return expr


# Test code
if __name__ == '__main__':
    queue = Queue()
    for i in range(10):
        queue.enqueue(i*i+1)
        print(queue)
    print()
    for i in range(10):
        a = queue.dequeue()
        print(a, end='\t')
        print(queue)
