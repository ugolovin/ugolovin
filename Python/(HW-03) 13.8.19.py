tiket = int(input("Введите количество билетов:\n"))
price=0
for i in range(tiket):
    print("Введите возраст", i+1,"-го поситетеля:")
    age = int(input())
    if 18 <= age >= 25:
        price = price + 990
    elif age > 25:
        price = price + 1390
if tiket > 3:
    price = price * 0.9
print("Общая стоимость всех билетов: ", '%-6.2f' % (price),"руб")