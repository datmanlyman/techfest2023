import random
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self, data):
        node = Node(data)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def insertTail(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = node

    def popHead(self):
        if self.head is None:
            print("There is nothing!")
            return

        node = self.head
        next = self.head.next
        next.prev = None
        self.head.next = None
        self.head = next

        return node

    def view(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


def LaplaceSmoothing(numberOfEach):  # Should be a single integer per row
    totalNumber = sum(numberOfEach)  # For the total number

    for idx in range(len(numberOfEach)):
        numberOfEach[idx] = (numberOfEach[idx] + 1) / \
            (totalNumber + 5)  # (n + 1)/(N + V)

    return numberOfEach  # Should become floats


def PlotLine(probabilityOfEach):
    line = []
    total = 0

    for probability in probabilityOfEach:
        # range for each job class is inclusive of total + number
        line.append(total + probability)
        total += probability

    return line


def GetJobType(line):
    randomNumber = random.random()
    for idx in range(len(line)):
        endNumber = line[idx]
        if randomNumber <= endNumber:
            return idx
    return 0


def GetJob(jobQueues, line):
    seen = [0 for _ in range(5)]
    jobClass = GetJobType(line)
    seen[jobClass] = 1
    jobQueue = jobQueues[jobClass]
    while not jobQueue:
        jobClass = GetJobType(line)
        if seen[jobClass] == 1:
            print(f"{jobClass} has already been accessed")
            continue
        seen[jobClass] = 1
        jobQueue = jobQueues[jobClass]
        if not jobQueue and sum(seen) == 5:
            print("All empty!")
            return
    return jobQueue.popleft()


def SetJob(viewQueue):
    node = viewQueue.popHead()
    return node.data


numberOfEach = [3, 3, 1, 1, 2]
probabilityOfEach = LaplaceSmoothing(numberOfEach)
line = PlotLine(probabilityOfEach)
jobQueues = [deque([i]) for i in range(5)]
viewQueue = DoublyLinkedList()
for _ in range(6):
    viewQueue.insertTail(GetJob(jobQueues, line))

viewQueue.view()
