class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} say "meow"')


if __name__ == "__main__":
    tom = Cat("murzik", 25)
    tom.meow()
    
    
    