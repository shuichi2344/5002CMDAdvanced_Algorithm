import threading
import random
import time

# Function to simulate a task: generates a list of 100 random integers (1-1000)
# Includes a small sleep delay to simulate processing time
def generate_random_numbers():
    time.sleep(0.001)
    return [random.randint(1, 1000) for _ in range(100)]

# Function to be run by each thread
# Stores the result in the shared results list at a given index
# Records the start and end time of the thread
def thread_function(results, index, start_times, end_times):
    start_times[index] = time.time_ns()         # Record start time
    results[index] = generate_random_numbers()  # Perform the task
    end_times[index] = time.time_ns()           # Record end time

# Runs the task using multithreading over 10 rounds and returns the time taken for each round
def run_multithreading():
    times = []
    for _ in range(10):
        results = [None] * 3           # Store results from threads
        start_times = [0] * 3          # Store start times for each thread
        end_times = [0] * 3            # Store end times for each thread
        threads = []

        # Create and start 3 threads
        for i in range(3):
            t = threading.Thread(target=thread_function, args=(results, i, start_times, end_times))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # Calculate total duration for this round (from earliest start to latest end)
        t1 = min(start_times)
        t2 = max(end_times)
        times.append(t2 - t1)  # Append total time taken
    return times

# Runs the same task sequentially (no threads) over 10 rounds
def run_non_multithreading():
    times = []
    for _ in range(10):
        start = time.time_ns()  # Start time for the round
        for _ in range(3):
            generate_random_numbers()  # Run task 3 times sequentially
        end = time.time_ns()
        times.append(end - start)  # Append total time taken
    return times

# Prints a side-by-side comparison of multithreaded and non-multithreaded results
def print_comparison(mt_times, non_mt_times):
    print("Round-by-Round Performance Comparison:")
    print("+--------+------------------------+-----------------------------+---------------------+")
    print("| Round  | Multithreading Time (ns) | Non-Multithreading Time (ns) | Difference (ns)     |")
    print("+--------+------------------------+-----------------------------+---------------------+")

    for i in range(10):
        diff = mt_times[i] - non_mt_times[i]  # Compute time difference
        print(f"| {i+1:<6} | {mt_times[i]:<22} | {non_mt_times[i]:<27} | {diff:<19} |")

    print("+--------+------------------------+-----------------------------+---------------------+\n")

    # Calculate and print summary statistics
    total_mt = sum(mt_times)
    total_non_mt = sum(non_mt_times)
    avg_mt = total_mt / 10
    avg_non_mt = total_non_mt / 10
    diff_total = total_mt - total_non_mt
    diff_avg = avg_mt - avg_non_mt

    print("Summary of Results:")
    print("+-------------+---------------------+--------------------------+----------------------+")
    print("| Metric      | Multithreading (ns) | Non-Multithreading (ns) | Difference (ns)       |")
    print("+-------------+---------------------+--------------------------+----------------------+")
    print(f"| Total Time  | {total_mt:<19} | {total_non_mt:<24} | {diff_total:<20} |")
    print(f"| Average Time| {avg_mt:<19} | {avg_non_mt:<24} | {diff_avg:<20} |")
    print("+-------------+---------------------+--------------------------+----------------------+")

# Entry point of the program
if __name__ == "__main__":
    mt_times = run_multithreading()          # Run and collect multithreading timings
    non_mt_times = run_non_multithreading()  # Run and collect single-threaded timings
    print_comparison(mt_times, non_mt_times) # Display results
