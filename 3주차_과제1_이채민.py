import sys
input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.array = [0 for i in range(100000)]
        self.length = 0
    def add(self, number):
        self.length+=1
        self.array[self.length] = number
        self.up_sort(self.length)
    def delete(self):
        if not self.length:
            print(0)
            return
        print(self.array[1])
        self.array[1] = self.array[self.length]
        self.length-=1
        if self.length:
            self.down_sort(1)
    def down_sort(self, idx):
        if idx>=self.length or idx*2>self.length:
            return 
        min_index = idx*2
        if idx*2+1 <= self.length:
            min_index = idx*2+1 if self.array[idx*2]>self.array[idx*2+1] else idx*2
        if self.array[min_index] < self.array[idx]:
            self.array[min_index], self.array[idx] = self.array[idx], self.array[min_index]
            self.down_sort(min_index)
        else: 
            return 
    def up_sort(self, idx):
        if idx==1 or self.length == 1:
            return
        if self.array[idx]<self.array[idx//2]:
            self.array[idx], self.array[idx//2] = self.array[idx//2], self.array[idx]
            self.up_sort(idx//2)
        else:
            return 

# main
cnt = int(input())
heap = Heap()
for i in range(cnt):
    num = int(input())
    if(num!=0):
        heap.add(num)
    else:
        heap.delete()