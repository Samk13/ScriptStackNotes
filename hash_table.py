
from operator import le
from textwrap import indent


INTIAL_CAPACITY = 50


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.capacity = INTIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    def hash(self, key):
        hashsum = 0
        for idx, c in enumerate(key):
            hashsum += (idx + len(key)) ** ord(c)
        return hashsum % self.capacity

    def insert(self, key, value):
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
            return
        prev = node
        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)

    def find(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next
        if node is None:
            return
        return node.value

    def remove(self, key):
        index = self.hash(key)
        node = self.buckets[index]
        if node is None and node.key != key:
            prev = node
            node = node.next
        if node is None:
            return
        else:
            self.size -= 1
            result = node.value
            if prev is None:
                node = None
            else:
                prev.next = node.next.next
            return result

    def get_all_keys(self):
        result = []
        for bucket in self.buckets:
            node = bucket
            while node is not None:
                result.append((node.key, node.value))
                node = node.next
        return result

    def insert_multiple(self, keys, values):
        for key, value in zip(keys, values):
            self.insert(key, value)


x = HashTable()
x.insert('123123', 1)
x.insert('b', 2)
x.insert('c', 3)
x.insert('d', 4)
x.insert('e', 5)
x.insert('f', 6)
x.insert('g', 7)
x.insert('h', 8)
x.insert('i', 9)
x.insert('j', 10)
x.insert('k', 11)
x.insert('l', 12)
x.insert('m', 13)
x.insert_multiple(['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], [
                  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26])
print(x.find('a'))
print(x.get_all_keys())
