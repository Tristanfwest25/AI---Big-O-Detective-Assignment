"""
Exercise: Big O Detective
Module 2 — Advanced Python & Data Handling
Estimated time: 25 minutes

Objective: Analyze Python functions and classify their time complexity,
then write and benchmark two duplicate-finding functions.
"""

import time


# ============================================================
# PART 1 — Classify These Functions
# For each function, fill in the Big O and explain why.
# ============================================================

def get_first(data):
    return data[0]

# Big O: ___O(1)
# Reason: ___Grabbing item 0 is one operation, which takes constant time regardless of the list size.


def count_matches(data, target):
    count = 0
    for item in data:
        if item == target:
            count += 1
    return count

# Big O: ___O(n)
# Reason: ___The function goes through the list only once, so the time it takes grows linearly with the size of the list.


def all_pairs(data):
    pairs = []
    for i in data:             # outer loop
        for j in data:         # inner loop
            pairs.append((i, j))
    return pairs

# Big O: ___O(n²)
# Reason: ___There are two nested loops, each going through the list, so the time grows quadratically with the size of the list.


def mystery(n):
    steps = 0
    while n > 1:
        n = n // 2
        steps += 1
    return steps

# Big O: ___O(log n)
# Reason: ___The function repeatedly halves n until it reaches 1, so the number of steps grows logarithmically with the size of n.


def process(data):
    total = sum(data)
    ordered = sorted(data)
    pos = ordered.index(total) if total in ordered else -1
    return pos

# Big O: ___O(n log n)
# Reason: ___The sum() function is O(n), sorted() is O(n log n), and index() is O(n) in the worst case. The sorting dominates, so the overall complexity is O(n log n).


# ============================================================
# PART 2 — Write and Benchmark Two Duplicate Finders
# ============================================================

def has_duplicates_slow(data):
    """Check for duplicates using nested loops. Should be O(n²).

    Args:
        data: A list of numbers
    Returns:
        True if any duplicates exist, False otherwise
    """
    
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return True
    return False
            
        


def has_duplicates_fast(data):
    """Check for duplicates using a set. Should be O(n).

    Args:
        data: A list of numbers
    Returns:
        True if any duplicates exist, False otherwise
    """
  
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


def benchmark(func, data, label):
    """Time a function call and return elapsed milliseconds."""
    start = time.time()
    result = func(data)
    elapsed = (time.time() - start) * 1000
    print(f"  {label:<25} result={result}  time={elapsed:.3f} ms")
    return elapsed


# ============================================================
# BENCHMARKING — run this after implementing both functions
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("Duplicate Detection Benchmark")
    print("=" * 60)
    print(f"  {'Function':<25} {'Result':<14} {'Time'}")
    print(f"  {'-'*25} {'-'*14} {'-'*12}")

    for size in [1000, 5000, 10_000]:
        # Build a list with no duplicates, then force one at the very end.
        # Putting the duplicate last is worst-case for the slow version.
        test_data = list(range(size))
        test_data.append(size - 1)   # duplicate of the last element

        print(f"\n  Size = {size:,}:")
        t_slow = benchmark(has_duplicates_slow, test_data, "has_duplicates_slow")
        t_fast = benchmark(has_duplicates_fast, test_data, "has_duplicates_fast")

        if t_slow and t_fast:
            print(f"  → Fast version was {t_slow / t_fast:.1f}x faster")
            
            
# Benchmark Output
"""Duplicate Detection Benchmark
============================================================
  Function                  Result         Time
  ------------------------- -------------- ------------

  Size = 1,000:
  has_duplicates_slow       result=True  time=12.809 ms
  has_duplicates_fast       result=True  time=0.073 ms
  → Fast version was 175.0x faster

  Size = 5,000:
  has_duplicates_slow       result=True  time=305.726 ms
  has_duplicates_fast       result=True  time=0.447 ms
  → Fast version was 684.6x faster

  Size = 10,000:
  has_duplicates_slow       result=True  time=1142.210 ms
  has_duplicates_fast       result=True  time=0.564 ms
  → Fast version was 2024.0x faster"""