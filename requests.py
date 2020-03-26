#Скачайте файл. В нём указан адрес другого файла, который нужно скачать с использованием модуля requests и посчитать число строк в нём.
#Используйте функцию get для получения файла (имеет смысл вызвать метод strip к передаваемому параметру, чтобы убрать пробельные символы по краям).
#После получения файла вы можете проверить результат, обратившись к полю text. Если результат работы скрипта не принимается, проверьте поле url на правильность. Для подсчёта количества строк разбейте текст с помощью метода splitlines.
#В поле ответа введите одно число или отправьте файл, содержащий одно число.

import requests
with open('input.txt', 'r') as input:
    str = input.readline().strip()
r = requests.get(str)
lst = r.text.splitlines()
print(lst)


#Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
#Первое слово в тексте последнего файла: "We".
#Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.
#Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

import requests
resource = 'https://stepic.org/media/attachments/course67/3.6.3'
is_finish = False
filename = 'https://stepic.org/media/attachments/course67/3.6.3/699991.txt'
while (is_finish == False):
    if (filename != 'We'):
        print('NO')
        r = requests.get(filename)
        filenamelst = r.text
        print(filenamelst)
        filename = filenamelst
        filename = resource + '/' + filename
        print(filename)
    else:
        print('YES')
        r = requests.get(filename)
        print(r.text)
        is_finish = True
