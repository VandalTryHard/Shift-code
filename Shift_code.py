"""Задача
Код сдвига — один из самых простых кодов, который может использоваться для шиф-
рования сообщений. Каждая буква заменяется другой буквой, полученной сдвигом
вперед по алфавиту на заданную величину. Например, при сдвиге на один символ
строка «abc» преобразуется в «bcd» (то есть каждая буква в алфавите сдвигается вперед на одну позицию).
Напишите программу, которая выводит следующее меню:
1) Make a code
2) Decode a message
3) Quit
Enter your selection:
Если пользователь выбирает вариант 1, он получает возможность ввести сообщение
(с пробелами), а затем число. Python выводит закодированное сообщение, полученное
с применением заданного сдвига.
Если пользователь выбирает вариант 2, он вводит закодированное сообщение и правильное число, а программа
выводит декодированное сообщение (то есть смещается на нужное количество букв в обратном направлении по
алфавиту).
При выборе варианта 3 программа завершает работу.
После того как пользователь закодирует или декодирует сообщение, меню выводится снова, пока пользователь не
завершит работу с программой.
Для выполнения этой задачи необходимы следующие навыки:
ввод и вывод данных;
списки;
разбиение и соединение строк;
инструкции if;
циклы (while и for);
подпрограммы.
"""

start = True
# list_ = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
# "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
list_ = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", 
"т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", " "]

def main():
    while start:
        print("1) Make a code")
        print("2) Decode a message")
        print("3) Quit")
        user_choice = input("Enter: ")
        if user_choice == "1":
            code_mes, num_shift = make_code()
            code(code_mes, num_shift)
        elif user_choice == "2":
            code_mes, num_shift = make_code()
            decode_message(code_mes, num_shift)
        elif user_choice == "3":
            quit()
        else:
            print("ValueError")

def make_code():
    code_mes = input("Message: ")
    code_mes = code_mes.lower()
    num_shift = int(input("How many signs to shift (1-33): "))#для англ 26
    if num_shift == 0 or num_shift > 33: #для англ 26
        while num_shift > 0 and num_shift < 33: #для англ 26
            num_shift = int(input("ValueError. Try 1-33: "))#для англ 26
    data = code_mes, num_shift
    return(data)
    
def code(code_mes, num_shift):
    new_mes = ""
    for i in code_mes:
        x = list_.index(i)
        x = x + num_shift
        if x > 33: #для англ 26
            x = x - 34 #для англ 27
        symbol = list_[x]
        new_mes = new_mes + symbol
    print(new_mes)
    return(new_mes)
        
def decode_message(code_mes, num_shift):
    message = ""
    for i in code_mes:
        x = list_.index(i)
        x = x - num_shift
        if x > 33: #для англ 26
            x = x + 34 #для англ 27
        symbol = list_[x]
        message = message + symbol
    print(message)
    return(message)

main()
