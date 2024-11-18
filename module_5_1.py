class House:
    def __init__(self, name, number_of_floors):         # создаем интерпритато
        self.name = name                            # задаем 1ю переменную
        self.number_of_floors = number_of_floors    # задаем 1ю переменную

    def go_to(self, new_floor):                     # объявляем метод
        print(f'{self.name} имеет {self.number_of_floors} этажей. Едем на {new_floor} этаж:')
        if new_floor > self.number_of_floors or new_floor < 1:          # создаем условие, когда выводим несуществующий этаж
            print(f'{new_floor} - Такого этажа нет')
        else:
            for floor in range(1, new_floor + 1):                        # выводим количество этажей, при существующем этаже (ЭТУ КОНСТРУКЦИЮ НАШЛА В ИНТЕРНЕТЕ)
                print(floor)

h1 = House('ЖК Ильинка', 25)
h2 = House('ЖК Авиатор', 10)

h1.go_to(5)
h2.go_to(20)