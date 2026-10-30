def calculate_delivery(subtotal, express=False):
    if not isinstance(subtotal, int) or isinstance(subtotal, bool):
        raise TypeError("subtotal должен быть целым числом")
    if not isinstance(express, bool):
        raise TypeError("express должен быть логическим значением")
    if subtotal < 0:
        raise ValueError("Сумма заказа не может быть отрицательной")

    if subtotal < 1000:
        cost = 300
    elif 1000 <= subtotal <= 5000:
        cost = 150
    else:
        cost = 0

    if express:
        cost += 250

    return cost
