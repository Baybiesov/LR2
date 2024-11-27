salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

total = 0

# Цикл для расчета расходов на каждый месяц
for month in range(months):
    total += spend
    spend *= (1 + increase)

emergency_fund = total - (salary * months)

if emergency_fund < 0:
    emergency_fund = 0

emergency_fund = round(emergency_fund)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {emergency_fund}")
