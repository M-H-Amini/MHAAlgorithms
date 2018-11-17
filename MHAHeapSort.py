# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:36:11 2018

@author: MHA
"""

from MHAMaxHeap import MHAMaxHeap as Heap

def MHAHeapSort(array):
    heap=Heap(array)
    heap.buildMaxHeap()
    for i in range(heap.heap_size-1,-1,-1):
        temp=heap.array[heap.heap_size-1]
        heap.array[heap.heap_size-1]=heap.array[0]
        heap.array[0]=temp
        heap.heap_size-=1
        heap.maxHeapify(0)
    return heap.array

a=[20,30,19,40,25,15,14,50,1]
a = MHAHeapSort(a)
print(a)