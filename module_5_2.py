class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        print(f'{self.name} имеет {self.number_of_floors} этажей. Едем на {new_floor} этаж:')
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f'{new_floor} - Такого этажа нет')
        else:
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return self.name




h1 = House('ЖК Ильинка', 25)
h2 = House('ЖК Авиатор', 10)
print(len(h1))
print(len(h2))
print(f'{h1}, количество этажей: {len(h1)}')
print(f'{h2}, количество этажей: {len(h2)}')

# h1.go_to(5)
# h2.go_to(20)
