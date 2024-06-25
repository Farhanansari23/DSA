class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a linked list.

    Attributes:
    - head: The head node of the linked list.

    Methods:
    - __init__(self): Initializes an empty linked list.
    - insert_at_beginning(self, data): Inserts a new node at the beginning of the linked list.
    - insert_at_end(self, data): Inserts a new node at the end of the linked list.
    - print(self): Prints the elements of the linked list.
    - insert_values(self, data): Inserts multiple values into the linked list.
    - length(self): Returns the length of the linked list.
    - remove_at(self, index): Removes a node at the specified index from the linked list.
    - insert_at(self, index, data): Inserts a new node at the specified index in the linked list.
    - index_of(self, data): Returns the index of the first occurrence of the specified data in the linked list.
    - insert_after(self, after, data): Inserts a new node after the node with the specified data in the linked list.
    - remove_by_value(self, data): Removes the first occurrence of the specified data from the linked list.
    """

    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the linked list.

        Args:
        - data: The data to be stored in the new node.
        """
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the linked list.

        Args:
        - data: The data to be stored in the new node.
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node



    def print(self):
        """
        Prints the elements of the linked list.
        """
        if self.head is None:
            print("The list is empty")
            return
        
        itr = self.head
        log = ""
        while itr:
            log += ( str(itr.data) + "-->")
            itr = itr.next
        print(log)

    def insert_values(self, data):
        """
        Inserts multiple values into the linked list.

        Args:
        - data: A list of values to be inserted into the linked list.
        """
        self.head = None
        for i in data:
            self.insert_at_end(i)

    def length(self):
        """
        Returns the length of the linked list.

        Returns:
        - The length of the linked list.
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        """
        Removes a node at the specified index from the linked list.

        Args:
        - index: The index of the node to be removed.

        Raises:
        - Exception: If the index is out of range.
        """
        if index >= self.length() or index < 0:
            raise Exception("Index out of range!")
        
        if index == 0:
            if self.head:
                self.head = self.head.next
            return
        
        cu_index = 0
        itr = self.head
        while itr:
            if cu_index + 1 == index:
                itr.next = itr.next.next
                break
            itr = itr.next
            cu_index += 1

    def insert_at(self, index, data):
        """
        Inserts a new node at the specified index in the linked list.

        Args:
        - index: The index at which the new node should be inserted.
        - data: The data to be stored in the new node.

        Raises:
        - Exception: If the index is out of range.
        """
        node = Node(data)
        if index >= self.length() or index < 0:
            raise Exception("Index out of range!")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        cu_index = 0
        itr = self.head
        while itr:
            if index == cu_index+1:
                node.next = itr.next.next
                itr.next = node
                break

            itr = itr.next
            cu_index += 1

    def index_of(self, data):
        """
        Returns the index of the first occurrence of the specified data in the linked list.

        Args:
        - data: The data to search for in the linked list.

        Returns:
        - The index of the first occurrence of the data, or None if the data is not found.
        """
        count = 0
        itr = self.head
        while itr:
            if itr.data == data:
                return count
            itr= itr.next
            count += 1

    def insert_after(self, after, data):
        """
        Inserts a new node after the node with the specified data in the linked list.

        Args:
        - after: The data of the node after which the new node should be inserted.
        - data: The data to be stored in the new node.
        """
        itr = self.head
        while itr:
            if itr.data == after:
                node = Node(data)
                node.next = itr.next
                itr.next = node
                break
            itr= itr.next
    

    def remove_by_value(self, data):
        """
        Removes the first occurrence of the specified data from the linked list.

        Args:
        - data: The data to be removed from the linked list.
        """
        if self.head.data == data:
            self.head = self.head.next
            return
        itr = self.head
        while itr:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr= itr.next
            


if __name__ == '__main__':
    linkedList = LinkedList() # create a linked list
    linkedList.insert_at_beginning(5) # insert a node at the beginning
    linkedList.insert_at_end(10) # insert a node at the end
    linkedList.insert_values([1, 2, 3, 4, 5]) # insert multiple values
    linkedList.print() # print the linked list
    linkedList.remove_at(2) # remove a node at index 2
    linkedList.print() # print the linked list
    linkedList.insert_at(2, 100) # insert a node at index 2
    linkedList.print() # print the linked list
    print(linkedList.index_of(100)) # get the index of a node with value 100
    linkedList.insert_after(100, 200) # insert a node after a node with value 100
    linkedList.print() # print the linked list
    linkedList.remove_by_value(200) # remove a node with value 200
    linkedList.print() # print the linked list