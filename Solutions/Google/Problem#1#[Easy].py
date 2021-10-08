#coding problem 1

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?




def is_add_up(li,ki):
    l = len(li)
    result = []
    for i in li:
        a = li.index(i)
        b = 0
        for largo in range(a,l):
            if i + li[(a+b)] == ki:
                yield(f"True since {ki} = {i} + {li[(a+b)]}")
                b +=1
            else:
                b +=1
    

list = [10,15,3,7]
k = 17

for i in is_add_up(list,k):
    print(i)
