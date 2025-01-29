# Задача "За честь и отвагу!"

import threading

class Knight(threading.Thread):
    
    def __init__(self, name, power, enemy=100):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = enemy

    def hostile(self, name, power, enemy):
        day = 0
        while enemy:
            enemy -= power
            day += 1
            print(f'{name}, сражается {day} день(дня)..., осталось {enemy} воинов.\n\r', end='')
        print(f'{name} одержал победу спустя {day} дней(дня)!\n\r', end='')

    def run(self):
        self.hostile(self.name, self.power, self.enemy)


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились')



