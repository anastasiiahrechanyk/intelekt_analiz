# Початкові дані 
sales = [100, 110, 125, 120, 135, 150]
periods = list(range(1, len(sales) + 1))

# Список
growth_coeff = []     
growth_rate = []       
increase_rate = []     

for i in range(1, len(sales)):
    k = sales[i] / sales[i - 1]
    t_growth = k * 100
    t_increase = t_growth - 100

    growth_coeff.append(k)
    growth_rate.append(t_growth)
    increase_rate.append(t_increase)

# Середній рівень ряду
avg_sales = sum(sales) / len(sales)

# Середній абсолютний приріст
avg_increase = (sales[-1] - sales[0]) / (len(sales) - 1)

# Середній темп зростання (геометричний)
avg_growth_rate = (sales[-1] / sales[0]) ** (1 / (len(sales) - 1)) * 100
avg_increase_rate = avg_growth_rate - 100

# Результат
print("Ланцюгові показники динаміки:")
print(f"{'Період':<8}{'Ki(зр)':<10}{'Ti(зр), %':<12}{'Ti(пр), %':<12}")
for i in range(1, len(sales)):
    print(f"{periods[i]:<8}{growth_coeff[i-1]:<10.3f}{growth_rate[i-1]:<12.1f}{increase_rate[i-1]:<12.1f}")

print("\nУзагальнюючі показники:")
print(f"Середній обсяг продажів: {avg_sales:.2f} тис. грн")
print(f"Середній абсолютний приріст: {avg_increase:.2f} тис. грн")
print(f"Середній темп зростання: {avg_growth_rate:.2f}%")
print(f"Середній темп приросту: {avg_increase_rate:.2f}%")
