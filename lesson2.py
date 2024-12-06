class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return (f'name: {self.name} age: {self.age}'
                f'brith year: {2024 - self.age}')

some_animal = Animal('anim', 12)
print   (some_animal.info())