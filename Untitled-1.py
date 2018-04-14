class persona():
    def __init__(self, name, sirname):
        self.name = name
        self.sirname = sirname
    def get_full_name(self):
        return f'{self.name} {self.sirname}'
John = persona('John', 'Doe')
print(John.get_full_name())
class student(persona):
    def __init__(self, name, sirname, class_room):
        super().__init__(name, sirname)
        self.calss_room = class_room
Alis = student('Alis', 'Cooper', '7b')
print(Alis.get_full_name())