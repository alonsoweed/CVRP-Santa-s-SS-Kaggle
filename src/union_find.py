
def union(x, y):
    x_root = find(x)
    y_root = find(y)
    
    joined_demand = x_root.demand + y_root.demand
    
    if x.is_first() and y.is_first():
        joined_first = x_root.last 
        joined_last = y_root.last
    elif x.is_first() and y.is_last():
        joined_first = y_root.first 
        joined_last = x_root.last
    elif x.is_last() and y.is_first():
        joined_first = x_root.first 
        joined_last = y_root.last
    elif x.is_last() and y.is_last():
        joined_first = x_root.first 
        joined_last = y_root.first
            
    if x_root.rank > y_root.rank:
        y_root.parent = x_root
    elif x_root.rank < y_root.rank:
        x_root.parent = y_root
    elif x_root != y_root:  
        y_root.parent = x_root
        x_root.rank = x_root.rank + 1
        
    x_new_root = find(x_root)
    x_new_root.first = joined_first
    x_new_root.last = joined_last
    x_new_root.demand = joined_demand

def find(x):
    if x.parent == x:
        return x
    else:
        x.parent = find(x.parent)
        return x.parent

def joinable(capacity, x, y):
    x_root = find(x)
    y_root = find(y)
    return (x_root != y_root) and ((x_root.demand + y_root.demand) <= capacity) and x.is_end() and y.is_end()

class path:
    def __init__(self, demand, val):
        self.val = val
        self.first = val
        self.last = val
        self.parent = self
        self.rank = 0
        self.demand = demand
    
    def is_end(self):
        root = find(self)
        return (self.val == root.first) or (self.val == root.last)
    
    def is_first(self):
        root = find(self)
        return self.val == root.first
    
    def is_last(self):
        root = find(self)
        return self.val == root.last

    

