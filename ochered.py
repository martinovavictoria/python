class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} добавлен в стек")

    def pop(self):
        if self.top is None:
            print("Стек пуст")
            return None

        value = self.top.data
        self.top = self.top.next
        print(f"{value} удалён")
        return value

    def peek(self):
        return self.top.data if self.top else "Пусто"
        
class StoreQueue:
    def __init__(self):
        self.front = None 
        self.rear = None 

    def enqueue(self, customer_name):
        new_node = Node(customer_name)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"{customer_name} встал в очередь.")

    def dequeue(self):
        if self.front is None:
            print("Очередь пуста")
            return None
        customer = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Покупатель {customer} обслужен.")
        return customer

    def peek(self):
        return self.front.data if self.front else "Пусто"
    
class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_front(self, data): # Как в стеке
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail: self.tail = new_node

    def add_rear(self, data): # Как в очереди
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def remove_front(self): # Как в очереди/стеке
        if not self.head: return None
        val = self.head.data
        self.head = self.head.next
        if not self.head: self.tail = None
        return val

stack = Stack()

stack.push("Книга")
stack.push("Тетрадь")
stack.push("Ручка")

print(stack.peek())

stack.pop()

print(stack.peek())
