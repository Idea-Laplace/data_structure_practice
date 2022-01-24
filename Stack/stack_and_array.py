# class Stack
class Element:
    def __init__(self, item):
        self.data = item
        self.prev = None


class Stack:
    def __init__(self):
        self.depth = 0
        self.peek = None

    def push(self, element: Element):
        self.depth += 1
        if self.peek:
            element.prev = self.peek
        self.peek = element

    def pop(self):
        if not self.depth:
            raise ValueError

        extract = self.peek
        if extract.prev:
            self.peek = extract.prev
        else:
            self.peek = None
        self.depth -= 1
        return extract

    def __repr__(self):
        if not self.depth:
            return ']'
        elem = self.peek
        rep = str(elem.data)
        while elem.prev:
            rep += '|'
            rep += str(elem.data)
            elem = elem.prev
        rep += ']'
        return rep



# class Array

class Array:
    def __init__(self, size: int, type, fixed=True):
        self.size = size
        self.length = 0
        self.type = type
        self.fixed = fixed

    def append(self, data):
        if self.type != type(data):
            raise ValueError('You input wrong datatype.')
        if self.length < self.size:
            self.__setattr__(f'index_{self.length}', data)
            self.length += 1
            return True
        elif self.fixed:
            return IndexError(f'Index out of range: {self.size}')
        else:
            self.__setattr__(f'index_{self.length}', data)
            self.length += 1
            self.size += self.size

    def index(self, idx: int):
        if idx >= 0 and idx < self.length:
            return self.__getattribute__(f'index_{idx}')
        elif idx < 0 and idx >= -self.length:
            return self.__getattribute__(f'index_{self.length+idx}')
        else:
            raise IndexError

    def pop(self, idx=-1):
        if not self.length:
            raise IndexError
        value = self.index(idx)
        if idx < 0:
            idx = self.length + idx
        for i in range(idx, self.length-1):
            temp = self.__getattribute__(f'index_{i+1}')
            self.__setattr__(f'index_{i}', temp)
        self.__setattr__(f'index{self.length-1}', None)
        self.length -= 1
        return value

    def insert(self, idx: int, value):
        if self.length >= self.size:
            if self.fixed:
                raise IndexError(f'Index out of range: {self.size}')
            else:
                self.size += self.size
        if self.type != type(value):
            raise ValueError('You input wrong datatype.')
        if idx > self.length or idx < -self.length:
            raise IndexError
        elif idx >= 0:
            for i in range(self.length, idx, -1):
                self.__setattr__(f'index_{i}', self.__getattribute__(f'index_{i-1}'))
            self.__setattr__(f'index_{idx}', value)
        else:
            new_idx = self.length + idx
            for i in range(self.length, idx, -1):
                self.__setattr__(f'index_{i}', self.__getattribute__(f'index_{i-1}'))
            self.__setattr__(f'index_{new_idx}', value)
        self.length += 1

    def find(self, obj):
        for idx in range(self.length):
            if self.index(idx) == obj:
                return idx
        return False

    def delete(self, obj):
        for idx in range(self.length):
            if self.index(idx) == obj:
                self.pop(idx)
                return True
        return False

