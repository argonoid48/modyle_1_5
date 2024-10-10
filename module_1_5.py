# Практическое задание по теме "Неизменяемые и изменяемые объекты. Кортежи"
# Андрей Галкин
immutable_var = 100,200,300, True, 'TEXT'       # Это кортеж.
print(immutable_var)
mmutable_var[2]= 50000                          # Изменим 300 на 50000.
                                                #
                                                # File "E:\UU\PROJECT\iesson_01\.venv\module_1_5.py",
                                                # line 5, in <module>
                                                #     mmutable_var[2]= 50000
                                                #     ^^^^^^^^^^^^
                                                # NameError: name 'mmutable_var' is not defined. Did you mean: 'immutable_var'?
                                                # В кортеже значения данных менять нельзя.

mutable_list = [500, 600, 700, True, 'DIALOG']  # Это список.
print(mutable_list)
mutable_list[1]= 1000                           # Изменяем 600 на 1000.
print(mutable_list)                             # Всё ОК. Список можно изменить.


