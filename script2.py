class Dispositivo:
    def __init__(self, id=None, nombre=None, marca=None, tipo=None, diccionario=None):
        if diccionario:
            self.id = diccionario["id"]
            self.nombre = diccionario["nombre"]
            self.marca = diccionario.get("marca")
            self.tipo = diccionario.get("tipo")
        else:
            self.id = id
            self.nombre = nombre
            self.marca = marca
            self.tipo = tipo
            
class Database:
    def __init__(self, template):
        self.database = [Dispositivo(diccionario=d) for d in template["dispositivos"]]
    def delete_by_id(self, id):
        self.database = [d for d in self.database if d.id != id]
    def add_dispositivo(self, diccionario):
        dispositivo = Dispositivo(diccionario=diccionario)
        self.database.append(dispositivo)