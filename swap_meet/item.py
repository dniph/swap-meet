import uuid  # Importamos el módulo para generar IDs únicos

class Item:
    def __init__(self, id=None, condition=0):
        # Si no se provee un id, genera uno único usando uuid
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id = id
        # Inicializa la condición del item
        self.condition = condition

    def get_category(self):
        # Retorna el nombre de la clase como categoría
        return self.__class__.__name__

    def __str__(self):
        # Retorna string con información básica del item
        return f"An object of type {self.__class__.__name__} with id {self.id}."

    def condition_description(self):
        # Diccionario con descripciones de condición
        descriptions = { # Think these are supposed to be doubles..?
            0.0: "Poor",
            1.0: "Fair",
            2.0: "Good",
            3.0: "Very Good",
            4.0: "Like New",
            5.0: "Mint"
        }
        # Retorna la descripción correspondiente o mensaje default
        return descriptions.get(self.condition, "Unknown condition")
