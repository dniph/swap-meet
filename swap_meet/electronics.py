from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id = None, condition=0, type="Unknown"):
        super().__init__(id)
        self.condition = condition
        self.type = type
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} This is a {self.type} device."