class intSet(object):
    def __init__(self):
        self.vals = []
    def insert(self,e):
        if not e in self.vals:
            self.vals.append(e)
    def  member(self,e):
        return e in self.vals
    def remove(self,e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+'not found')
    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    def __len__(self):
        return len(self.vals)
    def intersect(self,s1):
        s2 = intSet()
        for i in self.vals:
            for j in s1.vals:
                if i == j:
                    s2.vals.append(i)
        return s2
        
