"""
This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
"""
import time

def job_scheduler(f,n):
    time.sleep(n/1000)
    f()

#example function
def funct():
    for i in range(5):
        print(i)

print(job_scheduler(funct, 3000))
