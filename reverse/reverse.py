class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution
        # Check if there is already a head, or a next for the head
        if not self.head or not self.head.next_node:
            return self.head
        # define variable to initial head
        current_node = self.head
        # define variable to previous_node
        previous_node = None
        # Loop through the list
        while current_node:
            # define variable to hold next node of head
            next_node = current_node.next_node
            # set the heads next node to previous node
            current_node.next_node = previous_node
            # update previous_node to head
            previous_node = current_node
            # updat the head now to be the next node
            current_node = next_node
        # now set the previous_node back to the head
        self.head = previous_node
    