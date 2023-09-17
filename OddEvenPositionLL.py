# o group odd nodes together and even nodes together talking about its position not value

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def group_nodes_by_position(head):
    if head is None or head.next is None:
        return head

    odd_head = head
    even_head = head.next
    odd_current = odd_head
    even_current = even_head

    while even_current is not None and even_current.next is not None:
        odd_current.next = even_current.next
        odd_current = odd_current.next

        even_current.next = odd_current.next
        even_current = even_current.next

    odd_current.next = even_head

    return odd_head

def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" ")
        current = current.next
    print()

# Example usage
if __name__ == "__main__":
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
    head = Node(1)
    current = head
    for i in range(2, 7):
        current.next = Node(i)
        current = current.next

    print("Original list:")
    print_list(head)

    head = group_nodes_by_position(head)

    print("Grouped list:")
    print_list(head)
