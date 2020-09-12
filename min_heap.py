# Course: CS261 - Data Structures
# Assignment: 5
# Student: Luwey Hon
# Description: This program represent a min heap which
# is like a tree but all nodes child must be greater than
# the parent's node. It implements several ADTS for
# the min heap.


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:
    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.heap = DynamicArray()

        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0

    def add(self, node: object) -> None:
        """
        Adds a new node into the min heap
        """

        # in case there's one node and dont need to find a previous
        if self.heap.length() == 0:
            self.heap.append(node)
            return

        self.heap.append(node)


        # finding the previous and current index as well as its value
        prev_index = (self.heap.length() // 2 - 1)
        curr_index = self.heap.length() - 1
        prev = self.heap.get_at_index(prev_index)
        current = self.heap.get_at_index(curr_index)

        # swapping the elments
        while current < prev and curr_index != 0:
            self.heap.swap(prev_index, curr_index)
            curr_index = prev_index

            # outlier when prev_index is right before root, need to assign to root
            if prev_index == 1:
                prev_index -= 1
            # update prev index after swapping
            else:
                prev_index = (prev_index + 1) // 2 - 1

            # update previous node
            prev = self.heap.get_at_index(prev_index)

        pass

    def get_min(self) -> object:
        """
        returns minimum key without removing it
        """

        if self.heap.length() == 0:
            raise MinHeapException

        return self.heap.get_at_index(0)

    def remove_min(self) -> object:
        """
        Removes the minimum key and updates the
        positions after removing
        """

        # when the heap is empty
        if self.heap.length() == 0:
            raise MinHeapException

        curr_index = 0

        # base cases when removing  1,2,3 nodes
        if self.heap.length() == 1:
            pop_val = self.heap.pop()
        elif self.heap.length() == 2:
            self.heap.swap(0, 1)
            pop_val = self.heap.pop()
        elif self.heap.length() == 3:
            # if left is smaller
            if self.heap.get_at_index(1) < self.heap.get_at_index(2):
                self.heap.swap(0, 1)
                self.heap.swap(1,2)
                pop_val = self.heap.pop()
            # if right is smaller
            else:
                self.heap.swap(1,2)
                pop_val = self.heap.pop()

        # removing when there's 4+ nodes
        else:
        # swapping the last node with the front, and then popping to remove it
            self.heap.swap(0, self.heap.length() - 1)
            pop_val = self.heap.pop()

            # finding the direction in the first swap
            if self.heap.get_at_index(1) > self.heap.get_at_index(2):
                next = self.heap.get_at_index(2)
                next_index = 2
            else:
                next = self.heap.get_at_index(1)
                next_index = 1

            current = self.heap.get_at_index(curr_index)
            next = self.heap.get_at_index(next_index)
            curr_index = 0
            flag = 1

            while flag == 1:

                # initial first swap
                if curr_index == 0:
                    self.heap.swap(curr_index, next_index)
                    curr_index = next_index
                    # if self.heap.length() <= 3:
                    #     flag = 0

                # swaps afterwards
                else:
                    # keeping track of left and right nodes
                    left = (curr_index + 1) * 2
                    right = left + 1

                    # it reaches the bottom of the tree
                    if (curr_index + 1) * 2 + 1> self.heap.length():
                        flag = 0

                    # when theres a left node but no right node
                    elif (curr_index + 1) * 2 == self.heap.length():
                        if self.heap.get_at_index(curr_index) > self.heap.get_at_index(self.heap.length() - 1):
                            self.heap.swap(curr_index, self.heap.length() - 1)
                            flag = 1

                    # swapping to the left node when the left node is smaller
                    else:
                        # finding the values of the left, right, and current node
                        left_val = self.heap.get_at_index(left - 1)
                        right_val = self.heap.get_at_index(right - 1)
                        curr_val = self.heap.get_at_index(curr_index)

                        # moves left in the tree
                        if left_val > right_val and curr_val > right_val:
                            self.heap.swap(curr_index, right - 1)
                            curr_index = right - 1

                        # moves right in the tree
                        elif right_val > left_val and curr_val > left_val:
                            self.heap.swap(curr_index, left - 1)
                            curr_index = left - 1

                        # else its in the right spot
                        else:
                            flag = 0

        return pop_val

    def build_heap(self, da: DynamicArray) -> None:
        """
        Builds a Min heap by a given unsorted dynamic array
        """

        # making a new DA and keeping track of length
        new_da = DynamicArray()
        length = da.length()
        for pos in range(length):
            new_da.append(da.get_at_index(pos))

        # removing the current heap
        for _ in range(self.heap.length()):
            self.heap.pop()

        # initializing it by finding the first parent node at bottom of tree
        parent = (length - 1) // 2 - 1
        left = parent * 2 + 1
        right = left + 1

        # working backwards until it reach the tree node
        while parent >= 0:

            # finding if the left or right is smaller
            if new_da.get_at_index(left) > new_da.get_at_index(right):
                small = right
            else:
                small = left

            old_parent = parent
            flag = 0

            # percolating down to see if the node need to be swapped
            while new_da.get_at_index(parent) > new_da.get_at_index(small) and flag != 1:
                new_da.swap(parent, small)
                parent = small
                try:
                    left = parent * 2 + 1
                    right = left + 1
                    if new_da.get_at_index(left) > new_da.get_at_index(right):
                        small = right
                    else:
                        small = left

                    if parent > small:
                        new_da.swap(parent,small)
                except:
                    flag = 1

            # going on to the next parent node
            parent = old_parent - 1
            left = parent * 2 + 1
            right = left + 1

        # building the new heap
        for pos in range(length):
            self.heap.append(new_da.get_at_index(pos))

        pass


# BASIC TESTING
if __name__ == '__main__':

    # print("\nPDF - add example 1")
    # print("-------------------")
    # h = MinHeap()
    # print(h, h.is_empty())
    # for value in range(300, 200, -15):
    #     h.add(value)
    #     print(h)
    #
    # print("\nPDF - add example 2")
    # print("-------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
    #     h.add(value)
    #     print(h)


    # print("\nPDF - get_min example 1")
    # print("-----------------------")
    # h = MinHeap(['fish', 'bird'])
    # print(h)
    # print(h.get_min(), h.get_min())

    #
    # print("\nPDF - remove_min example 1")
    # print("--------------------------")
    # h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    # while not h.is_empty():
    #     print(h, end=' ')
    #     print(h.remove_min())
    #
    # #
    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    # da = DynamicArray([32,12,2,8,16,20,24,40,4])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)

