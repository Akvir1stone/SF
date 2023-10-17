class Client:
    def __init__(self, name, f_name, city, cash):
        self.name = name
        self.f_name = f_name
        self.city = city
        self.cash = cash

    def __str__(self):
        return f'{self.name} {self.f_name}, {self.city}, Cash: {self.cash} rub'

    def get_info(self):
        return f'{self.name} {self.f_name}, {self.city}'


cl1 = Client('Ivan', 'Petrov', 'Moscow', '50')
cl2 = Client('Ivan2', 'Petrov2', 'Moscow', '50')
cl3 = Client('Ivan3', 'Petrov3', 'Moscow', '50')
cl4 = Client('Ivan4', 'Petrov4', 'Moscow', '50')
print(cl1)
list_of_cl = [cl1, cl2, cl3, cl4]
for i in list_of_cl:
    print(i.get_info())
