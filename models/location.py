class Location:
    
    def __init__(self, name, user, set, filmed = False, good_climate = False, id = None):
        self.name = name 
        self.set = set 
        self.filmed = filmed 
        self.good_climate = good_climate
        self.id = id 
        self.user = user
        
        
    def mark_filmed(self):
        self.filmed = True
    
    def mark_good_climate(self):
        self.good_climate = True



