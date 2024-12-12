import tkinter as tk # tkinter - это библиотека графического интерфейса
# Вторая часть. Наделение кнопок ГИ функциональной направленностью



# def add(): # Создадим функцию для сложения.
#     # num1 = int(number1_entry.get()) # Метод get позволяет вытащить ту информаци, которую пользователь напишет в данном окне. Чтоб хранить информацуию, надо создать переменную с этими значениями/ понятно, чстобы у нас программа воспринимала число, а не текст, надо указать команду int
#     # num2 = int(number2_entry.get())
#     # # print(num1 + num2) # Если мы просто запишем программу так. То ничего не произойдёт. Чтобы связать функцию с ГИ надо в соответствующей строке с кнопкой указать параметр command = add (в данном случае со сложением)
#     # res = num1 + num2 # Чтобы отразить результат данной функции, надо создать переменную res (например) и задать формулу его получения. И результат надо вставить в соответсующее поле для ответа ГИ.
#     # answer_entry.insert(0, res) # Чтобы вствить результат в соответвующее поле воспользуемся методом insert где указываем сначала куда мы указываем результат (индекс), а потом что мы указываем (res)
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     res = num1 + num2
#     answer_entry.delete(0, 'end') # Чтобы значения постоянно обновлялись, исопльзуют метод delete - он позволяет удалять отработанную операцию. Записывается в два значения (начало и конец)
#     answer_entry.insert(0, res)
# # Давайте создадим функции и для других кнопок по принципу примера с плюсом
# def sub():
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     res = num1 - num2
#     answer_entry.delete(0,'end')
#     answer_entry.insert(0, res)
#
# def mul():
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     res = num1 * num2
#     answer_entry.delete(0, 'end')
#     answer_entry.insert(0, res)
#
# def div():
#     num1 = int(number1_entry.get())
#     num2 = int(number2_entry.get())
#     res = num1 / num2
#     answer_entry.delete(0, 'end')
#     answer_entry.insert(0, res)

# Способ 2.

# Чтобы избавиться от повторяющихся действий для них можно записать отдельные функции. Для чисел и для очистки и заполнения полей.
def get_values(): # Создадим возвращающую функцию get_values со знакомыми нам значениями num1 и num2, к которым ф-я будет возвращаться при обращении
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2
 # Создадим принимающую функцию для очистки и добавления полей ГИ
def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

 # Тогда ф-я add будет иметь следующий вид после объединения всех трёх функций:
def add():
     num1, num2 = get_values()
     res = num1 + num2
     insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)



def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)




#  Первая часть - создание графического интерфейса
window = tk.Tk() # - чтобы создать окно в графическом интерфейче (ГИ) надо написать команду как мы видим в данносм примере с классом Tk
window.title('Калькулятор') # метод смены имени.обратим внимание, что смену названия вызваннного окошка я пишу в строке под командой вызова ГИ
# напомню, метод пишется после переменной, отделяясь от неё точкой как показано в примере выше
window.geometry('350x350') # этот метод задаёт размеры всплывающего окна ГИ
window.resizable(False, False) # метод, клоторый не даёт изменять размеры ГИ
button_add = tk.Button(window, text="+", width=2, height=2, command=add) # Данная команда позволяет в поле ГИ размещать дробные элементы. В нашем случае виджеты кнопок. Ей можно придать имя с помощью параметра text, а также размеры с помощью параметров width и height
button_add.place(x=100, y=200) # Метод который графически добавляет виджеты в поле ГИ по заданным координатам. Координаты записываются с верхнего левого угла. То есть будет х=0 и у=0.
# Кроме метода place есть и другие методы размещения виджетов в поле ГИ: pack, grid
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)
button_sub.place(x=150, y=200)
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)
button_mul.place(x=200, y=200)
button_div = tk.Button(window, text="/", width=2, height=2, command=div)
button_div.place(x=250, y=200)
number1_entry = tk.Entry(window, width=28) # Эта команда создаёт текстовое поле в ГИ. По сути это однострочное текстовое поле. Здесь также можно задавать параметры. Принадлежность ГИ window, а также ширину width и высоту height
number1_entry.place(x=100, y=75)
number2_entry = tk.Entry(window, width=28)
number2_entry.place(x=100, y=140)
answer_entry = tk.Entry(window, width=28)
answer_entry.place(x=100, y=270)
number1 = tk.Label(window, text="Введите первое число:") # Команда Label из библиотеки Tk позволяет использовать надписи
number1.place(x=100, y=50)
number2 = tk.Label(window, text="Введите второе число:")
number2.place(x=100, y=115)
answer = tk.Label(window, text="Ответ:")
answer.place(x=100, y=245)
window.mainloop() # - mainloop - метод, который обновляет информацию о происходящем на экране. Это важно, так как написание программ будет проходить между этой командой и самой первой функцией, где мы будем наполнять наш калькулятор иными командами


# Теперь научимся наш калькулятор вносить в исполняемый файл для обычного пользователя. Воспользуемся терминалом и введём туда следующую команду: pip install auto-py-to-exe


