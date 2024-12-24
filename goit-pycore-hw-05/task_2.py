import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r'\b\d+\.\d+|\b\d+\b', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

text = "Загальний дохід працівника: 1000.01 основний дохід, 27.45 бонус, 324.00 інші надходження."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")
