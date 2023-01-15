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


def LaplaceSmoothing(numberOfEach):  # Should be a single integer per row
    totalNumber = sum(numberOfEach)  # For the total number

    for idx in range(len(numberOfEach)):
        numberOfEach[idx] = (numberOfEach[idx] + 1) / \
            (totalNumber + 5)  # (n + 1)/(N + V)

    return numberOfEach  # Should become floats


def PlotLine(numberOfEach):
    line = []
    total = 0

    for number in numberOfEach:
        # range for each job class is inclusive of total + number
        line.append(total + number)
        total += number

    return line


def GetJobType(line):
    randomNumber = random.random()
    jobClass = float('inf')
    for idx in range(len(line)):
        endNumber = line[idx]
        if randomNumber <= endNumber:
            jobClass = idx
            break

    return jobClass
