class CircularListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


if __name__ == '__main__':
    head = CircularListNode(1)
    head.next = head

    print()
