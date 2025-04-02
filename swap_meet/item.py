import uuid  # Importamos el módulo para generar IDs únicos

class Item:
    def __init__(self, id=None, condition=0, age=0):

        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

        self.condition = condition
        self.age = age

    def get_category(self):

        return self.__class__.__name__

    def __str__(self):

        return f"An object of type {self.__class__.__name__} with id {self.id}."

    def condition_description(self):

        descriptions = { 
            0.0: "Poor",
            1.0: "Fair",
            2.0: "Good",
            3.0: "Very Good",
            4.0: "Like New",
            5.0: "Mint"
        }

        return descriptions.get(self.condition, "Unknown condition")
