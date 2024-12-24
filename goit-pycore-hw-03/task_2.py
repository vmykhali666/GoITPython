import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000) or not (min <= quantity <= max):
        return []
    return sorted(random.sample(range(min, max + 1), quantity))

print(get_numbers_ticket(1, 49, 6))