class Character:
    def __init__(self, name, x, y, health):
        self.__name = name
        self.__x = x
        self.__y = y
        self.__health = health

    @property
    def name(self):
        return self.__name
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def health(self):
        return self.__health
    @health.setter
    def health(self, health):
        if 0 < health <= 100:
            self.__health = health
        else:
            print('Ошибка')



    def move(self, direction):
        if direction == 'w':
            self.__y += 1
        elif direction == 's':
            self.__y -= 1
        elif direction == 'd':
            self.__x += 1
        elif direction == 'a':
            self.__x -= 1
        else:
            print('Ошибка')

    def print_move(self):
        print(f'{self.name} со здоровьем {self.health} перешел в точку с координатами ({self.x}, {self.y})')

def main():
    name = input('Введите имя игрока: ')
    health = int(input('Введите здоровье игрока: '))
    print('Введите изначальные координаты игрока')
    x = int(input('x: '))
    y = int(input('y: '))
    character = Character(name, x,y, health)
    while True:
        stop = input('Введите + если хотите передвинуть игрока, - если хотите завершить ')
        if stop == '+':
            direction = input('Введите направление движения:\nw - вверх, d - вправо, s - вниз, a - влево\n')
            character.move(direction)
            character.print_move()
        elif stop == '-':
            break
        else:
            print('Ошибка')
main()