'''
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def largest(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr)
    pre2 = arr[0]
    pre1 = max(arr[0], arr[1])
    
    for i in range(2, n):
        curr = max(pre1, arr[i] + pre2)
        pre2, pre1 = pre1, curr
    return pre1

print(largest([5,1,1,5]))
print(largest([3,5]))
print(largest([3]))
print(largest([2,4,6,2,5]))
