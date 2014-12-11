"""
*** INCOMPLETE ***
Christina Chan
--
1) Min-Heap implementation
2) Read data from file, split by tokens, store as integers in a 2D list
3) Calculate lower bounds
    Row/Column Reduction Method
    ? Method
4) Calculate upper bounds
    Sum Diagonal Method
    Greedy Heuristic Method
5) Main
"""
##########################
# 1) Min Heap Class      #
##########################

class Min_Heap(object):
    def __init__(self):
        self.heap = []
        
    def getSize(self):
        return len(self.heap)
            
    def getHeap(self):
        return self.heap
            
    def getMin(self):
        size = self.getSize() - 1
        if size == -1:
            return None
        elif size == 0:
            return self.heap.pop(o)
        else:
            min = self.heap[0]
            self.heap[0] = self.heap.pop(size)
            self.heapify(0)
            return min
                    
    def insert(self, value):
        # when inserting values, value must be a list
        self.heap.append(value)
        index = self.getSize() - 1
        parent_index = int((index-1)/2)
        while index != 0 and self.heap[parent_index][0] > self.heap[index][0]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = int((index-1)/2)

    def remove(self, index):
        size = self.getSize() - 1
        self.heap[index] = self.heap.pop(size)
        self.heapify(index)
            
    def heapify(self, index):
        size = self.getSize()
        left_child = (index*2) + 1
        right_child = left_child + 1
        smallest = index
        if left_child < size and self.heap[left_child][0] < self.heap[smallest][0]:
            smallest = left_child
        if right_child < size and self.heap[right_child][0] < self.heap[smallest][0]:
            smallest = right_child
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify(smallest)

##########################
# 2) Process Data File   #
##########################

def read_data(my_list, my_file):
    for line in my_file:
        line_list = list()
        for token in line.split():
            line_list.append(int(token))
        my_list.append(line_list)

##########################
# 3) Lower Bound         #
##########################

def row_col_redux(my_list):
    n = my_list[0][0]
    lower_bound = 0
    # reduce rows
    for i in range(1, n+1):
        min_val = min(my_list[i])
        lower_bound += min_val
        for j in range(0, n):
            my_list[i][j] = my_list[i][j] - min_val
    # reduce columns
    for x in range(0, n):
        col = list()
        for y in range(1, n+1):
            col.append(my_list[y][x])
        min_val = min(col)
        lower_bound += min_val
        for z in range(1, n+1):
            my_list[z][x] = my_list[z][x] - min_val
    return lower_bound

def method2(my_list):
    lower_bound = 0
    return lower_bound

##########################
# 4) Upper Bound         #
##########################

def sum_diagonal(my_list):
    n = my_list[0][0]
    upper_bound = 0
    for i in range(1, n+1):
        upper_bound += my_list[i][i]
    return upper_bound

def greedy(my_list):
    upper_bound = 0
    return upper_bound
    

##########################
#      Main Function     #
##########################
def main():
    my_list = list()
    f = open("data1.txt")
    read_data(my_list, f)
    f.close()

    for i in my_list:
        print i

    lower_bound = row_col_redux(my_list)
    print lower_bound

main()
