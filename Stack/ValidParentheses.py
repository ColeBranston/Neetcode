class stack:
    def __init__(self, array):
        self.stor = array

    def push(self, val):
        self.stor.append(val)

    def pop(self):
        temp = self.stor[-1]
        del self.stor[-1]
        return temp


s = "([{}])"

for i in range(len(s)//2):
