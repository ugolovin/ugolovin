per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = input("Введите сумму(money), которую вы планируете положить под проценты\n")
deposit=[]
keys=[]

print("|Банк  |Процентная ставка |Заработок |")
print("______________________________________")
for key in per_cent:
    i=round(0.01*per_cent.get(key)*float(money))
    deposit.append(i)
    keys.append(key)
    print('|%-6s|%-18.1f|%-10d|' % (key,per_cent.get(key),i))
    print("______________________________________")
print("Максимальная сумма, которую вы можете заработать — ",max(deposit),"в",keys[deposit.index(max(deposit))])
