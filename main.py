# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def left(i):
    return 2*i + 1


def right(i):
    return 2*i + 2


def parent(i):
    return int((i - 1)/2)


class Heap:
    def __init__(self):
        self.array = []

    def minHeapify(self, index):
        minimum = index
        l = left(index)
        r = right(index)
        if l in range(len(self.array)) and self.array[l].val < self.array[minimum].val:
            minimum = l
        if r in range(len(self.array)) and self.array[r].val < self.array[minimum].val:
            minimum = r
        if minimum != index:
            self.array[minimum], self.array[index] = self.array[index], self.array[minimum]
            self.minHeapify(minimum)

    def buildMinHeap(self, arr):
        self.array = arr
        for i in range(int(len(self.array)/2) - 1, -1, -1):
            self.minHeapify(i)
        return self.array

    def extractMin(self):
        n = len(self.array)
        if n == 0:
            return
        if n == 1:
            return self.array.pop()
        root = self.array[0]
        self.array[0] = self.array[-1]
        self.array.pop()
        self.minHeapify(0)
        return root

    # inserts nodes not numbers, you either use it or use buildheap and edit heapify (remove .val)
    def insert(self, value):
        self.array.append(value)
        i = len(self.array) - 1
        while i != 0 and self.array[i].val < self.array[parent(i)].val:
            self.array[i], self.array[parent(i)] = self.array[parent(i)], self.array[i]
            i = parent(i)

    def printHeap(self):
        print(self.array)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    """obj = Heap()
    print(obj.buildMinHeap([3, 9, 2, 1, 4, 5]))
    print(obj.extractMin())
    obj.printHeap()
    obj.insert(0)
    obj.printHeap()"""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
