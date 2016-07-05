import sys
import copy
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

    def find_duplicate(self):

        i = 0
        while i < self.arr_size:
            if self.arr[i] <= i:
                i =+1
            else :
                temp = self.arr[i]
                self.arr[i] = self.arr[temp]
                self.arr[temp] = temp


        #
        #   for ele in self.arr:
        #    if self.arr[ele] == ele:
        #       print ("Duplicate element", ele)
        #    else :
        #       temp =


def main():
    dd = Duplicate();

    dd.create_arr(7)

    dd.insert_ele(1)
    dd.insert_ele(5)
    dd.insert_ele(1)
    dd.insert_ele(2)
    dd.insert_ele(6)
    dd.insert_ele(3)
    dd.insert_ele(6)

    dd.find_duplicate()
    dd.print_ele()

if __name__ == '__main__':
    main()