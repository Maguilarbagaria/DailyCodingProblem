"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible.
"""
class lastorder:
    stack = []
    
    def __init__(self):
        self = self
        
    def record(self, order_id):
        self.order_id = order_id
        lastorder.stack.append(order_id)

    def get_last(self,i):
        if len(lastorder.stack) >= i:
            return lastorder.stack[-i]
        else:
            return(f"There aren't {i} orders. Actually there are only {len(lastorder.stack)} orders")

d = lastorder()
#adding orderd
d.record("1abc")
d.record("2abc")
d.record("3abc")
#getting orders
print(d.get_last(5))
print(d.get_last(2))
