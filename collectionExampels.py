from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

# Counter is returning a dictionary with the number of times each element appears in the list
a = "aaaaaaaaaabbbbbbbbsssssssscccccccc"
my_counter = Counter(a)
# print(my_counter.most_common(2))  # [('a', 10), ('b', 8), ('s', 8), ('c', 8)]


# namedtuple is a tuple that can be accessed by name
Point = namedtuple("Point", ["x", "y"])

pt1 = Point(1, 2)
pt2 = Point(3, 4)
# print(type(pt1))  # <class '__main__.Point'>
# print(pt1.x)  # 1

# OrderedDict is a dictionary that remembers the order in which keys were inserted
# it become less udesful after python 3.7
OrderedDict = OrderedDict()
OrderedDict["a"] = 1
OrderedDict["b"] = 2
OrderedDict["c"] = 3
OrderedDict["d"] = 4
OrderedDict["e"] = 5
# print(OrderedDict) OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# defaultdict is a dictionary that returns a default value if the key is not found
# it is useful for when you want to return a default value if the key is not found
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
d["c"] = 3
#  print(d['d'])  # 0

# deque is a double ended queue
# it is a list that can be accessed from both sides
# it is useful for implementing a queue
dq = deque()
dq.append(1)
dq.append(5)
dq.appendleft(6)
dq.append(6)
dq.pop()
dq.popleft()
dq.clear()
dq.extend([4, 5, 9])
dq.extendleft([4, 5, 3])
dq.extend([9, 6])
print("before rotate", dq)
dq.rotate(-1)
print("after  rotate", dq)
dq.rotate(-1)
print("after  rotate", dq)
