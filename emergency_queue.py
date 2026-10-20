class Patient:
    def __init__(self, name, urgency):
        self.name = name
        self.urgency = urgency



class MinHeap:
    def __init__(self):
        self.data = []

    def heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.data[index].urgency < self.data[parent].urgency:
                self.data[index], self.data[parent] = self.data[parent], self.data[index]
                index = parent
            else:
                break

    def heapify_down(self, index):
        size = len(self.data)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2
            if left < size and self.data[left].urgency < self.data[smallest].urgency:
                smallest = left
            if right < size and self.data[right].urgency < self.data[smallest].urgency:
                smallest = right
            if smallest == index:
                break
            self.data[index], self.data[smallest] = self.data[smallest], self.data[index]
            index = smallest




# Test your MinHeap class here including edge cases
