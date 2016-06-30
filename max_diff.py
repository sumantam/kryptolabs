import sys
import copy

class max_diff():

    def __init__(self):
        self.min = -1
        self.diff = -1
        self.array = []

    def initialize(self, arr):
        self.array = arr[:]

    def print_array(self):
        print(self.array)

    def find_max_diff(self):
        self.min = self.array[0]

        for ele in self.array:

            if ((ele - self.min) > self.diff):
                self.diff = ele - self.min

            if ele < self.min:
                self.min = ele

        return self.diff

def main():

    diff_obj = max_diff()

    mylist = [3,5, 10, 2, 4, 4, 4]
    diff_obj.initialize(mylist)
    diff_obj.print_array()
    val = diff_obj.find_max_diff()

    print("The max diff is :", val)

if __name__ == '__main__':
    main()