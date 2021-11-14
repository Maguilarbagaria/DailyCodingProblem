"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Snapchat.

Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""

h = [(0, 50), (30, 75), (60, 150), (75, 100)]

def rooms(time):
    starts = sorted(start for start, end in time)
    #0, 30, 60, 75
    ends = sorted(end for start, end in time)
    #50, 75, 100, 150

    current_max = 0
    current_overlap = 0

    i, j = 0, 0
    #creamos 2 pointers si el inicio de la clase es inferior al fin de la clase, sumamos 1 clase necesaria
    #si el inicio de la clase es superior al fin restamos el loop y  mantenemos el número de clases
    while i < len(time) and j < len(time):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1

    return current_max

print(rooms(h))
