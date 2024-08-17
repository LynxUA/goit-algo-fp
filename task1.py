class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        self.head = prev

    def sort(self):
        if self.head is None or self.head.next is None:
            return

        def merge_sort(node: Node):
            if node is None or node.next is None:
                return node

            middle = self.get_middle(node)
            next_to_middle = middle.next
            middle.next = None

            left = merge_sort(node)
            right = merge_sort(next_to_middle)

            sorted_list = self.sorted_merge(left, right)
            return sorted_list

        self.head = merge_sort(self.head)

    def get_middle(self, head: Node):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, left: Node, right: Node):
        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, left.next)

        return result

    def merge_sorted_lists(self, llist2):
        merged_list = LinkedList()
        merged_list.head = self.sorted_merge(self.head, llist2.head)
        return merged_list

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next


llist = LinkedList()
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список:")
llist.print_list()

llist.reverse()
print("\nЗв'язний список після реверсу:")
llist.print_list()

llist.sort()
print("\nЗв'язний список після сортування:")
llist.print_list()

llist2 = LinkedList()
llist2.insert_at_end(7)
llist2.insert_at_end(12)
llist2.insert_at_end(18)

print("\nДругий зв'язний список:")
llist2.print_list()

merged_list = llist.merge_sorted_lists(llist2)
print("\nЗлитий зв'язний список:")
merged_list.print_list()
