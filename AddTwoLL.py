class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def addTwoLists(first, second):
    first = reverse_linked_list(first)
    second = reverse_linked_list(second)

    result_head = None
    carry = 0

    while first is not None or second is not None:
        fdata = 0 if first is None else first.data
        sdata = 0 if second is None else second.data

        Sum = carry + fdata + sdata

        carry = 1 if Sum >= 10 else 0
        Sum = Sum if Sum < 10 else Sum % 10

        temp = Node(Sum)
        temp.next = result_head
        result_head = temp

        if first is not None:
            first = first.next
        if second is not None:
            second = second.next

    if carry > 0:
        temp = Node(carry)
        temp.next = result_head
        result_head = temp

    return result_head

def printLinkedList(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

# Taking input.
def takeInput():
    arr = list(map(int, input().strip().split(" ")))
    if arr[0] == -1:
        return None

    head = Node(arr[0])
    last = head

    for data in arr[1:]:
        if data == -1:
            break

        last.next = Node(data)
        last = last.next

    return head

# Example usage
T = int(input().strip())
for i in range(T):
    first = takeInput()
    second = takeInput()

    result = addTwoLists(first, second)
    result = reverse_linked_list(result)
    printLinkedList(result)
