# Домашняя работа к семинару 3, для выбора необходимой программы запустите код и введите номер программы для проверки.

# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# 0 не является ни четным, ни нечетным индексом

def ProgramOne():
    list = [1, 2, 3, 4, 5, 6]
    result = 1
    resultList = []
    for i in range(len(list)):
        if i % 2 != 0:
            result *= list[i]
            resultList.append(list[i])
    print(f'Список полученных элементов для подсчета = {resultList}')
    print(f'Результат = {result}')
    MainProgram()


# Задача 2 Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

def ProgramTwo():
    def ProgramTwo():
    list1 = [2, 3, 4, 5, 6]
    list2 = [2, 3, 5, 6]
    
    def calculateMultiplication(list):
        lastIndex = len(list) - 1
        couplesList = []
        if len(list) % 2 == 0:
            countIterations = int(len(list) / 2)
        else:
            countIterations = int((len(list) / 2) + 1)
        resultList = [None] * countIterations
        for i in range(countIterations):
            resultList[i] = list[i] * list[lastIndex]
            coupleNum = f'{list[i]} * {list[lastIndex]}'
            couplesList.append(coupleNum)
            lastIndex -= 1
        print(f'Пары произведений = {couplesList}')
        print(f'Результаты вычислений = {resultList}')
        
    print(f'Пример 1 {list1}')
    calculateMultiplication(list1)
    print(f'Пример 2 {list2}')
    calculateMultiplication(list2)
    MainProgram()


# Задача 3 Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

def ProgramThree():
    listNumbers = [1.1, 1.2, 3.1, 5, 10.01]
    newList = [None] * len(listNumbers)
    for i in range(len(listNumbers)):
        if listNumbers[i] % 1 != 0:
            newList[i] = round(listNumbers[i] % 1, 3)
    newList.remove(None)
    print(f'Результат = {max(newList) - min(newList)}')
    MainProgram()


# Задача 4 Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def ProgramFour():
    numStr = int(input('Введите число для перевода = '))
    result = ''
    while numStr != 0:
        result = str(numStr % 2) + result
        numStr //= 2
    print(result)
    MainProgram()


# Задача 5 Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

def fib(num, positive):
    if positive == 1:
        a = 1
        b = -1
        for i in range(num):
            a, b = b, a - b
    else:
        a = 0
        b = 1
        for _ in range(num):
            a, b = b, a + b
    return a


def ProgramFive():
    num = int(input('Задайте число = '))
    listFib = []
    for i in range(-num + 1, 1):
        listFib.append(fib(-i, 1))
    for i in range(num + 1):
        listFib.append(fib(i, 2))
    print(listFib)
    MainProgram()


# Основная программа
def MainProgram():
    print('Введите номер программы (1-5), либо введите "Q" для выхода.')
    program = input('Программа № = ')
    if program.lower() == 'q':
        print('До свидания!')
    elif program.isdigit():
        if int(program) == 1:
            ProgramOne()
        elif int(program) == 2:
            ProgramTwo()
        elif int(program) == 3:
            ProgramThree()
        elif int(program) == 4:
            ProgramFour()
        elif int(program) == 5:
            ProgramFive()
        else:
            print('Введен некорректный номер, попробуйте еще раз.')
            MainProgram()
    else:
        print('Ввод некорректен, пожалуйста, попробуйте еще раз.')
        MainProgram()


print('Здравствуйте!')
MainProgram()
