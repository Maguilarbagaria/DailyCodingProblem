"""
This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""

def largest_ss(substring, number):
    result = ''
    if number == 0:
        return ("0 as no characters allowed")
    if number == 1: 
        return(f"whatever character of the substring for example: {substring[-1]}")
    for i in range(len(substring)):
        for _ in range(i+1, len(substring)+1):
            list = set(substring[i:_])
            list1 = substring[i:_]
            if len(list) == number and len(list1)>len(result):
                result = list1

    return result

    

print(largest_ss('abcba',2))
print(largest_ss('abcba',1))
print(largest_ss('abcba',0))
print(largest_ss('abcbbsaaattt',2))
