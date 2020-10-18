# # class User:
# #   nombre = 'Luis'

# # Instance
# # user = User()
# # print(user.nombre)

# class User:
#   def __init__(self, name, lastname):
#     self.name = name
#     self.lastname = lastname

#   def sayName(self):
#     print('Hi, my name is ' + self.name, self.lastname)

# user = User('Luis', 'Alvarez')

# user.sayName()


# user2 = User('mr', 'LuisFer')

# user2.name = 'Luis'

# user2.sayName()

# # For delete the object
# del user2

# # print(user2)

# # Heritage
# # class Admin(User):
# #   def saySomething(self):
# #     print('Herencia in spanish')

# # admin = Admin('Luis', 'admin')
# # admin.sayName()

# # Exercise with Classes

# class Animal:  
#   def __init__(self, name, onomatopeya, type):
#     self.name = name
#     self.onomatopeya = onomatopeya
#     self.type = type
    
#   def saludo(self):
#     print("Hi I'm a", self.type, 'and my sound is', self.onomatopeya)


# class Cat(Animal)
# cat = Cat('Fluffy', 'miau', 'cat')
# cat.saludo()


# class Dog(Animal) 
# dog = Dog('Firulais', "wuff", 'dog')
# dog.saludo()

# class Bird(Animal)
# bird = Bird('Piolin', 'Silbido', 'bird')
# bird.saludo()