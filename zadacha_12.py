# Задача 12: Обединяване на два речника с продукти и количества;
# количествата на общите продукти се събират


def read_products(label):
    """Въвежда речник {продукт: количество} от клавиатурата."""
    count = int(input(f"Брой продукти в {label}: "))
    products = {}
    for i in range(count):
        name = input(f"  Име на продукт {i + 1}: ")
        qty = int(input(f"  Количество на {name}: "))
        products[name] = products.get(name, 0) + qty
    return products


store1 = read_products("първия речник")
store2 = read_products("втория речник")

merged = dict(store1)
for name, qty in store2.items():
    merged[name] = merged.get(name, 0) + qty

print("Първи речник: ", store1)
print("Втори речник: ", store2)
print("Обединен:     ", merged)
