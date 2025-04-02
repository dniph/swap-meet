from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id = None, condition=0, fabric="Unknown"):
        super().__init__(id)
        self.condition = condition
        self.fabric = fabric
    
    def __str__(self):
        parent_str = super().__str__()
        return f"{parent_str} It is made from {self.fabric} fabric."