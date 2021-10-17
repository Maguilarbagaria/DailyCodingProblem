#This problem was asked by Stripe.

#Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def who_is_left(arr):
    k =[]
    for i in arr:
        if i >= 0:
            k.append(i)
    a = min(k)
    b = max(k)
    q = 0
    for t in range(a, b+1):
        if t in k:
            q += 1
        else:
            return(t)
    if q == len(k):
        return(t+1)
            
    


lista = [3,4,-1,1]
listb = [1,2,0]

print(who_is_left(lista))
