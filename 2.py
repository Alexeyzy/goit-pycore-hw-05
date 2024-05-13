
import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r"\b\d+\.\d+\b"
    res = re.findall(pattern, text)
    for r in res:
        yield float(r)
        
def sum_profit(text: str, func: Callable):
    summa  = sum(func(text))  
    return summa

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
