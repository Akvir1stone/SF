from catClass import Cat, Dog
cat1 = Cat(name="Baron", gend='boy', age=2)
cat2 = Cat(name="Sam", gend='boy', age=2)

print(cat1.get_name())
print(cat1.get_gend())
print(cat1.get_age())
print()
print(cat2.get_name())
print(cat2.get_gend())
print(cat2.get_age())

dog = Dog(name='Muhtar', gend='boy', age=0)
print()
print(dog.get_pet())
