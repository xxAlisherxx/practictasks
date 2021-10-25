# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.
# Формат вывода результата:
# =до минуты: <s> сек;
# до часа: <m> мин <s> сек;
# до суток: <h> час <m> мин <s> сек;
# в остальных случаях: <d> дн <h> час <m> мин <s> сеs://www.epochconк.
# # Примеры/Тесты:
# #
# # duration = 53: 53 сек
# # duration = 153: 2 мин 33 сек
# # duration = 4153: 1 час 9 мин 13 сек
# # duration = 400153: 4 дн 15 час 9 мин 13 сек
# # Примечание:
# #
# # можете проверить себя здесь: httpverter.com/
# Алгоритм
#
# Вывод результата зависит только от того, будет ли введенная продолжительность меньше или больше минуты/часа/суток/дня. Т.о. надо определить в какой из диапазонов попадает введенная продолжительность: [0,1 минута], [1 минута, 1 час] [1 час, 1 день],[1 день и до бесконечности]. И в зависимости от выполненного условия - вывести результат.
# Подумайте о том, в какое условия должны попасть граничные значения: типа 60 секунд, 60 минут, 24 часа. Т.е. 60 минут это только 60 мин или 1 час 00 мин 00 сек? В условии явного требования нет. На ваш выбор.
# Подумайте о том, чтобы избежать повторных операций деления и умножения.
# Вы можете вводить продолжительность с клавиатуры или завести в код.
one_minute = 60
one_hour = 3600
one_day = 86400
one_week = 604800
one_month = 2629743
one_year = 31556926

duration = int(input('Укажите продолжительность в секундах: '))

if duration < one_minute:

    print(str(duration) + ' секунд')
elif one_minute <= duration and one_hour > duration:
    user_minute = duration // one_minute
    user_second = duration % one_minute

    print(str(user_minute) + ' минуты', str(user_second) + ' секунд')

elif duration >= one_hour and duration < one_day:
    user_hour = duration // one_hour
    duration = duration % one_hour
    user_minute = duration // one_minute
    user_second = duration % one_minute

    print(str(user_hour) + ' час' , str(user_minute) + ' минуты', str(user_second) + ' секунд')

elif duration >= one_day and duration < one_week:
    user_day = duration // one_day
    duration = duration % one_day
    user_hour = duration // one_hour
    duration = duration % one_hour
    user_minute = duration // one_minute
    user_second = duration % one_minute
    print(str(user_day) + ' день', str(user_hour) + ' часа', str() + ' минуты', str(user_second) + ' секунды')