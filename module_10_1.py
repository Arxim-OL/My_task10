# Задача "Потоковая запись в файлы"

import threading
import time
from time import sleep



def wite_words(word_count, file_name):
    file = open(file_name, 'w', encoding='utf-8')
    for i in range(word_count):
        file.write(f'Какое-то слово № {i}\n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
end_time = time.time()
print(f'Работа потоков {round(end_time - start_time, 6)}')


start_time = time.time()
flow1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
flow2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
flow3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))
flow4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))
flow1.start()
flow2.start()
flow3.start()
flow4.start()
flow1.join()
flow2.join()
flow3.join()
flow4.join()
end_time = time.time()
print(f'Работа потоков {round(end_time - start_time, 6)}')
