from random import random

def merge_sort(a):
    if len(a) == 1:
        return a
    if len(a) == 2:
        return sort_2_items(a)
    
    split = len(a) // 2
    left = merge_sort(a[:split])
    right = merge_sort(a[split:])
    return merge(left, right)

def sort_2_items(a):
    first, second = a[0], a[1]
    if first < second:
        return a[:]
    return [second, first]

def merge(left, right):
    l_i, r_i = 0, 0
    out = []
    while l_i < len(left) and r_i < len(right):
        left_val, right_val = left[l_i], right[r_i]
        
        if left_val < right_val:
            out.append(left_val)
            l_i+=1
            
        else:
            out.append(right_val)
            r_i+=1
    
    if l_i < len(left):
        out.extend(left[l_i:])

    if r_i < len(right):
        out.extend(right[r_i:])
    
    return out

unsorted = [1000*random() for i in range(100)]
print(unsorted)
print(merge_sort(unsorted))