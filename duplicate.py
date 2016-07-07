import sys
import copy
import math
import numpy

class Duplicate():

    def __init__(self):
        self.arr = []
        self.arr_size = 0
        self.curr_size = 0

    def  create_arr(self, n):
        self.arr_size = n
        self.arr.extend([None]*n)

    def insert_ele(self, val):
        if(val >= self.arr_size):
            print("Please give the correct value, the value is out of range")
        else:
            self.arr[self.curr_size] = val
            self.curr_size += 1

    def print_ele(self):
        print(self.arr)

    def swap(self, s1, s2):
        return s2, s1

#    def max_heapify(self, i):
#
#       l = (int)(2*i+1)
#        r = (int)(2*i + 2)
#
#        if l < self.arr_size and self.arr[l] > self.arr[i] :
#            largest = l
#        else:
#            largest = i
#
#        if r < self.arr_size and self.arr[r] > self.arr[largest]:
#            largest = r
#
#        if largest != i:
#            self.arr[i], self.arr[largest] = self.swap(self.arr[i], self.arr[largest])
#
#
#    def build_maxheap(self):
#        heap_size = math.floor(self.arr_size/2)
#
#        while heap_size >= 0 :
#            self.max_heapify(heap_size)
#            heap_size = heap_size - 1


    def find_duplicate(self):

        for  ele in  self.arr:
            if self.arr[abs(ele)] > 0 :
                self.arr[abs(ele)] = -self.arr[abs(ele)]
            else:
                print("Repeat ", abs(ele))
'''
        i = 0
        while i < self.arr_size:
            if self.arr[i] <= i :
                i = i+1
            else :
                temp = self.arr[i]
                self.arr[i] = self.arr[temp]
                self.arr[temp] = temp

                if self.arr[temp] == self.arr[i] :
                    print("Found a    Duplicate Object")

'''


def main():
    print("Starting the main  program")
    dd = Duplicate();

    dd.create_arr(7)

    dd.insert_ele(1)
    dd.insert_ele(5)
    dd.insert_ele(1)
    dd.insert_ele(2)
    dd.insert_ele(6)
    dd.insert_ele(3)
    dd.insert_ele(6)

    print("------ Before -----")
    dd.print_ele()

    #dd.find_duplicate()

    #dd.build_maxheap()
    #print("------ After  -----")
    dd.find_duplicate()
    dd.print_ele()

if __name__ == '__main__':
    main()
