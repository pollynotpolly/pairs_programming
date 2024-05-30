class Counter:
    def __init__(self):
        self.count = 0  #initailizes a counter 

    def add(self, num):    #adds to a single number to the counter 
        self.count += num
    
    def report(self):        #reports what its counted so far (behaviour)
        return f"Counted to {self.count} so far."