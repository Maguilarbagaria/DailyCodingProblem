"""
This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
#f(4) = 5, f(3) = 3, f(2)=2,  f(1) = 1 --> f(n) = f(n-2) + f(n-1)

def staircase(n): #much complexity and space
    if n == 0:
        return 1
    if n ==1:
        return 1
    else:
        return staircase(n-2)+staircase(n-1)

def dinamic(n): # para los steps 1 y 2.
    if n== 0 or n==1:
        return 1
    dp = [0] * n
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1]

def solution(n, steps):
    if n == 0 or n == 1:
        return 1
    dp = [0] * (n+1)
    dp[0] = 1
    print(dp)
    for i in range(1, n+1):     
        for j in steps:
            if i - j >= 0:
                dp[i] += dp[i-j]
    return dp

#print(dinamic(4))
#print(staircase(4))
print(solution(4,[1,3]))
