money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
months_without_debt = 0
while True:

    budget = salary + money_capital
    if spend > budget:
        break

    months_without_debt += 1
    money_capital -= (spend - salary)
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", months_without_debt)
