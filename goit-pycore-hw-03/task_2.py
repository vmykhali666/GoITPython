import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min < max <= 1000) or not (1 <= quantity <= (max - min + 1)):
        return []
    
    unique_numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(unique_numbers)

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

print(get_numbers_ticket(10, 11, 11))