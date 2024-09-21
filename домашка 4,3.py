def add(a,b):
    return a+b

def substruct(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    if b==0:
        return "Ошибка! На ноль делить нельзя"
    else:
        return a/b

def get_number(prompt):
    while True:
        value=input(prompt)
        if value.lstrip("-").isdigit():
            return int(value)
        else:
            print("Это не число!")

def log(result):
    try:
        with open("calc.txt",'a') as file:
            file.write(result+"\n")
    except Exception as e:
        print(f"Произошла  ошибка {e}")


print("Выберите операцию: ",'1.Сложение','2.Вычитание', '3.Умножение', '4.Деление', sep='\n')
valid=['1','2','3','4']
choice=None

while choice not in valid:
    choice=input("Введите номер операции(1/2/3/4): ")
    if choice not in valid:
        print("Вы ввели некорректное значение. Вы можете вводить только 1,2,3 или 4.")



    
n1=get_number("Введите первое число: ")
n2=get_number("Введите второе число: ")

if choice=="1":
    r=f'Результат: {n1} + {n2} = {add(n1,n2)}'
elif choice=="2":
    r=f'Результат: {n1} - {n2} = {substruct(n1,n2)}'
elif choice=="3":
    r=f'Результат: {n1} * {n2} = {multiply(n1,n2)}'
elif choice=="4":
    result=divide(n1,n2)
    if isinstance(result,str):
        print(result)
    else:
        r=f'Результат: {n1} / {n2} = {result}'
else:
    print("Такой операции не существует")

log(r)#передаем значение переменной r в функцию log, в параметр result







