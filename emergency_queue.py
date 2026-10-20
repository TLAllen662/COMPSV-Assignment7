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

    def insert(self, patient):
        self.data.append(patient)
        self.heapify_up(len(self.data) - 1)

    def peek(self):
        if not self.data:
            return None
        return self.data[0]

    def remove_min(self):
        if not self.data:
            return None
        root = self.data[0]
        last = self.data.pop()
        if self.data:
            self.data[0] = last
            self.heapify_down(0)
        return root

    def print_heap(self):
        print("Current Queue:")
        for patient in self.data:
            print(f"- {patient.name} ({patient.urgency})")




# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    heap = MinHeap()

    # Empty heap
    assert heap.peek() is None
    assert heap.remove_min() is None
    heap.print_heap()

    # Example from the assignment
    heap.insert(Patient("Jordan", 3))
    heap.insert(Patient("Taylor", 1))
    heap.insert(Patient("Avery", 5))
    heap.print_heap()
    next_up = heap.peek()
    assert (next_up.name, next_up.urgency) == ("Taylor", 1)
    assert len(heap.data) == 3  # peek doesn't remove

    served = heap.remove_min()
    assert served.name == "Taylor"
    heap.print_heap()
    assert [p.name for p in heap.data] == ["Jordan", "Avery"]

    # Single element, then empty again
    assert heap.remove_min().name == "Jordan"
    assert heap.remove_min().name == "Avery"
    assert heap.data == [] and heap.remove_min() is None

    # Duplicates and ordering
    for name, urgency in [("A", 4), ("B", 2), ("C", 2), ("D", 10), ("E", 1), ("F", 4)]:
        heap.insert(Patient(name, urgency))
    order = []
    while heap.data:
        order.append(heap.remove_min().urgency)
    assert order == [1, 2, 2, 4, 4, 10]

    print("All MinHeap tests passed.")
