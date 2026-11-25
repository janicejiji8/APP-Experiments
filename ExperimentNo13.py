import threading
import time

def count_numbers(limit):
    for i in range(1, limit + 1):
        print(f"Counting: {i}")
        time.sleep(0.5)

def calculate_squares(numbers):
    for num in numbers:
        print(f"Square of {num}: {num ** 2}")
        time.sleep(0.5)

def calculate_cubes(numbers):
    for num in numbers:
        print(f"Cube of {num}: {num ** 3}")
        time.sleep(0.5)

def main():
    numbers = [1, 2, 3, 4, 5]

    t1 = threading.Thread(target=count_numbers, args=(5,))
    t2 = threading.Thread(target=calculate_squares, args=(numbers,))
    t3 = threading.Thread(target=calculate_cubes, args=(numbers,))

    print("Starting all threads...\n")
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("\nAll threads have finished execution.")

if __name__ == "__main__":
    main()
