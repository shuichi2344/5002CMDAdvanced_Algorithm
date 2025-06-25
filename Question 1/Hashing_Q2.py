import random

def generate_random_ic() -> str:
    """Generate a random valid 12-digit Malaysian IC number (YYMMDD######)."""
    year = random.randint(50, 99) if random.random() < 0.5 else random.randint(0, 24)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    random_digits = random.randint(100000, 999999)
    return f"{year:02d}{month:02d}{day:02d}{random_digits}"

def hash_ic(ic: str, table_size: int) -> int:
    """Folding-based hash function using group of 4 digits."""
    group_size = 4
    # Fold the IC number by summing 4-digit chunks
    folded = sum(int(ic[i:i + group_size]) for i in range(0, len(ic), group_size))
    return folded % table_size

def simulate_with_output(table_size: int, rounds: int = 10, num_ics: int = 1000):
    """Simulate hash table insertions and print final table and collision rate."""
    total_collisions = 0
    final_table = [[] for _ in range(table_size)]

    for round_num in range(1, rounds + 1):
        table = [[] for _ in range(table_size)]
        collisions = 0

        for _ in range(num_ics):
            ic = generate_random_ic()
            index = hash_ic(ic, table_size)
            if table[index]:
                collisions += 1
            table[index].append(ic)

        total_collisions += collisions

        if round_num == rounds:
            final_table = table  # Save the last round's table for display

    avg_collision_rate = (total_collisions / (rounds * num_ics)) * 100
    return final_table, avg_collision_rate

def print_hash_table(table):
    print(f"\nHash Table with size {len(table)}:")
    for i, bucket in enumerate(table):
        if bucket:
            print(f"table[{i}] --> " + " --> ".join(bucket))
        else:
            print(f"table[{i}]")


# === Main Program ===
small_table_size = 1009
big_table_size = 2003

# Simulate and get final hash tables + average collision rates
small_table, small_rate = simulate_with_output(small_table_size)
big_table, big_rate = simulate_with_output(big_table_size)

# Print hash table contents (after last round)
print_hash_table(small_table)
print_hash_table(big_table)

# Print final collision rates
print(f"\nCollision Rate for Smaller Hash Table: {small_rate:.2f} %")
print(f"Collision Rate for Bigger Hash Table: {big_rate:.2f} %")
