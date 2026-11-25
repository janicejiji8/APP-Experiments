import gc
import tracemalloc

def create_objects():
    for _ in range(300):
        obj1 = [0] * 20000
        obj2 = [0] * 20000
        obj1.append(obj2)
        obj2.append(obj1)

def display_memory_usage(stage):
    current, peak = tracemalloc.get_traced_memory()
    print(f"{stage} -> Current memory: {current / (1024 * 1024):.2f} MB | Peak memory: {peak / (1024 * 1024):.2f} MB")

tracemalloc.start()

display_memory_usage("Initial memory usage")

create_objects()
display_memory_usage("After creating objects")

gc.set_debug(gc.DEBUG_STATS)

collected = gc.collect()
print(f"Garbage collector: collected {collected} unreachable objects.")
display_memory_usage("After garbage collection")

gc.set_debug(0)
tracemalloc.stop()
