class Animal:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return f"My name is {self._name}"

    def make_a_sound(self):
        return ''

    @property
    def age(self):
        return f'I am {self._age}'


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"My name is {self._name}, the dog."

    def make_a_sound(self):
        return 'Woofers.'

    @property
    def age(self):
        return f'I am {self._age} years old!'


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def name(self):
        return f"My name is {self._name}, I am a cat."

    def make_a_sound(self):
        return '(Nokia Tune plays...)'

    @property
    def age(self):
        return f'I am {self._age} years old yo!'
        
        
if __name__ == "__main__":
    fido = Dog("Fido", 5)
    meowscles = Cat('Meowscles', 3)
    print(fido.name) 
    print(fido.age)
    
    print(meowscles.name)
    print(meowscles.age)