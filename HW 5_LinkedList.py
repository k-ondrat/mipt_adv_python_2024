class Node:
    def __init__(self, data, next_element=None):
        self.data = data
        self.next_element = next_element

    def __repr__(self):
        return f"Element({self.data})"

class SingleLinkList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next_element

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError("Индекс вне диапазона")
        current = self.head
        for _ in range(index):
            current = current.next_element
        return current.data

    def __repr__(self):
        elements = []
        current = self.head
        while current:
            elements.append(repr(current))
            current = current.next_element
        return " -> ".join(elements)

    def add(self, data):
        new_element = Node(data)
        if not self.head:
            self.head = new_element
        else:
            current = self.head
            while current.next_element:
                current = current.next_element
            current.next_element = new_element
        self.size += 1

    def remove(self, index=None):
        if self.size == 0:
            raise IndexError("Список пуст")
        if index is None:
            index = self.size - 1
        if not 0 <= index < self.size:
            raise IndexError("Индекс вне диапазона")
        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next_element
        else:
            previous = self.head
            for _ in range(index - 1):
                previous = previous.next_element
            removed_data = previous.next_element.data
            previous.next_element = previous.next_element.next_element
        self.size -= 1
        return removed_data

    def insert(self, index, data):
        if not 0 <= index <= self.size:
            raise IndexError("Индекс вне диапазона")
        new_element = Node(data)
        if index == 0:
            new_element.next_element = self.head
            self.head = new_element
        else:
            previous = self.head
            for _ in range(index - 1):
                previous = previous.next_element
            new_element.next_element = previous.next_element
            previous.next_element = new_element
        self.size += 1

my_list = SingleLinkList()
my_list.add(6)
my_list.add(8)
my_list.add(9)
my_list.add(13)
print(my_list)

print(len(my_list))

print(my_list[1])

my_list.insert(1, 5)
print(my_list)

my_list.remove(1)
print(my_list)

for item in my_list:
    print(item) 