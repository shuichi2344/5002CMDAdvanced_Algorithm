# === Hash Function Using Folding Technique ===
def hash_function(ic: str, table_size: int = 1009) -> int:
    """
    Hash function using folding method:
    Splits the IC number into 4-digit chunks, sums them, then applies modulo with table size.
    """
    group_size = 4
    # Fold the IC number by summing 4-digit chunks
    folded = sum(int(ic[i:i + group_size]) for i in range(0, len(ic), group_size))
    return folded % table_size


# === Main Function to Handle Input, Insertion, and Output ===
def display_hash_table():
    """
    Handles user input, inserts into hash table, and displays the hash table content.
    """
    table_size = 1009 # Fixed size of hash table
    hash_table = [[] for _ in range(table_size)] # Initialize hash table with empty chains

    print("Enter Malaysian IC numbers (12 digits, no dash).")
    print("Press Enter without typing anything to finish input.\n")

    while True:
        ic = input("IC: ").strip()

        # Stop input on empty line
        if ic == "":
            break
        elif len(ic) != 12 or not ic.isdigit():
            print("Invalid IC number. Please enter a 12-digit number.")
        else:
            index = hash_function(ic, table_size)   # Compute hash index
            hash_table[index].append(ic)    # Insert using separate chaining
            print(f"Added: {ic} → table[{index}]")

    # Final display of the full hash table
    print(f"\nHash Table with size {table_size}:")
    for i, entries in enumerate(hash_table):
        if entries:
            print(f"table[{i}] --> " + " --> ".join(entries))
        else:
            print(f"table[{i}]")


# === Run Program ===
if __name__ == "__main__":
    display_hash_table()
