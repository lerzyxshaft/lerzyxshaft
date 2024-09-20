print("bublles" ,end="777")
print("helo salam \" ua\nl\ne\ni\nk\num")
print("nmbrs:", max(1, 2, 4, 5, 6, 7, 8, 3))
print("nmbrs:", min(1, 2, 4, 5, 6, 7, 8, 3))

#abs - перпеводить відє'мне число з дужок в додатні.
print("nmbrs:", abs(-1))

#pow - ставить число з дужок в степінь де перше цифра - число, друга - степінь в яку буде поставлене перше число.(заміняє "**")
print("nmbrs:", pow(5, 3))

#roud - округляє числа при діленні до 1ого символа

print("nmbrs:", round(22 / 3))

input(print("Рядок для отримання даних через запит користувача "))

#Урок 4
number1 = 7 #int
print("результат:") #str
del number1
#Створення змінної функції та видалення її через "/del"
number3 = 6
print("число", number3)
number2 = 5
print("число", number2)
#Вивід інформації через змінну
word = "Result:"
number = 4.35 #float
print(word, number)
#Вивід інформації через дві змінні
random = False #bool

#print(random + print) не можна додати, різні типи рядків

q = 5 #int
w= "5" #str
#Писать разом через додавання ці два значення неможна, щоб їх об'єднати використовуємо зміну значення до іншого типу

print(word, number, q + int(w))

#//////////////////////////////////////////////////////////////////////////////////////////////////////

number12 = int(input("Write the first number"))
number13 = int(input("Write the second number"))

#number13 += 5 Додає до числа введеного користувачем число поставлене після знаку рівності, в моєму випадку 5. В залежності від
#знаку поставленого перед знаком рівності можемо виконати різні дії з число введеним заздалегіть, множення додавання і т.д.


print(number12 + number13)
print(number12 - number13)
print(number12 / number13)
print(number12 * number13)
print(number12 ** number13)
print(number12 // number13)
