import uuid
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
        
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        
        # Remueve mi item de mi inventario
        self.remove(my_item)
        # Agrega mi item al inventario del otro vendedor
        other_vendor.add(my_item)

        # Remueve el item del otro vendedor de su inventario
        other_vendor.remove(their_item)
        # Agrega el item del otro vendedor a mi inventario
        self.add(their_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory: # empty inventory
            return False
        return self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])
    
    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.get_category() == category:
                category_items.append(item)
        return category_items

    def get_best_by_category(self, category):
        highest_condition = 0
        best_item = None

        category_items = self.get_by_category(category)
        for item in category_items:
            if item.condition > highest_condition:
                best_item = item
                highest_condition = item.condition
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        vendor_best = self.get_best_by_category(their_priority) # my best of their desired category
        other_vendor_best = other_vendor.get_best_by_category(my_priority)

        if not vendor_best or not other_vendor_best:
            return False
        
        return self.swap_items(other_vendor, vendor_best, other_vendor_best)