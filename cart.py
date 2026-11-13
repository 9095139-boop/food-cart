"""Модуль кошика застосунку доставки їжі (user story US-3: Додавання страв у кошик).

Критерій приймання: загальна сума замовлення підраховується автоматично.
"""


def cart_total(prices, discount=0):
    """Повертає суму кошика зі знижкою у відсотках.

    prices   – список цін страв (числа >= 0).
    discount – знижка у відсотках, від 0 до 100 включно.

    Некоректні вхідні дані піднімають ValueError.
    """
    if not isinstance(prices, (list, tuple)):
        raise ValueError("prices має бути списком цін")
    for price in prices:
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError(f"ціна має бути числом, отримано {price!r}")
        if price < 0:
            raise ValueError(f"ціна не може бути від'ємною: {price}")
    if isinstance(discount, bool) or not isinstance(discount, (int, float)):
        raise ValueError("знижка має бути числом")
    if not 0 <= discount <= 100:
        raise ValueError(f"знижка має бути в межах 0–100, отримано {discount}")

    total = sum(prices)
    return round(total * (1 - discount / 100), 2)
