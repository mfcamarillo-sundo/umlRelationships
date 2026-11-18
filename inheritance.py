class Animal:
    def eat(self):
        print("The animal is eating.")


# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        print("The dog is barking.")


dog = Dog()
dog.eat()
dog.bark()
