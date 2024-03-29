#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return f'Node({self.data})'


class LinkedList:

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list."""
        ll_str = ""
        for item in self.items():
            ll_str += f'({item}) -> '
        return ll_str

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: If self.is_empty() == True set the head and the tail to the new node
        # TODO: Else append node after tail
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node

    # def find(self, item):
    #     """Return True if the given item is present in this linked list, otherwise False."""
    #     current = self.head
    #     while current is not None:
    #         if current.data == item:
    #             return True
    #         current = current.next
    #     return False
    def find(self, finder):
        """Return found node or None."""
        current = self.head
        while current is not None:
            if finder(current.data):
                return current.data
            current = current.next
        return None


    def replace(self, old_item, new_item):
        """Replace the given old_item with the new_item if old_item is present."""
        current = self.head
        while current is not None:
            if current.data == old_item:
                current.data = new_item
            current = current.next

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError."""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data
        # Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        previous = None
        current = self.head
        while current is not None:
            if current.data == item:
                if previous is not None:
                    previous.next = current.next
                    if current.next is None:
                        self.tail = previous
                else:
                    self.head = current.next
                    if self.head is None:
                        self.tail = None
                return
            previous = current
            current = current.next
        raise ValueError('Item not found: {}'.format(item))
    # def delete(self, item):
    #     """Delete the given item from this linked list, or do nothing."""
    #     previous = None
    #     current = self.head
    #     while current is not None:
    #         if current.data == item:
    #             if previous is not None:
    #                 previous.next = current.next
    #                 if current.next is None:
    #                     self.tail = previous
    #             else:
    #                 self.head = current.next
    #                 if self.head is None:
    #                     self.tail = None
    #             return  # Return without raising an error if item is found
    #         previous = current
    #         current = current.next


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))
    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
