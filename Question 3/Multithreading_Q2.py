import random

def generate_random_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

# Example usage:
random_numbers = generate_random_numbers()
print(random_numbers)
