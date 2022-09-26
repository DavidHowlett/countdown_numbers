"""
This generates the test data. Please don't re-run this without good cause.
"""

import random
import time

import main

top_row = [25, 50, 75, 100]
bottom_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
all_numbers = top_row + bottom_row


def time_to_solve(problem):
    start_time = time.perf_counter()
    # this makes progress visible
    print(problem)
    print(main.solution_to_string(main.solve(problem)))
    return time.perf_counter() - start_time


problems = [
    (random.sample(all_numbers, 7), random.randrange(100, 999)) for _ in range(100)
]

# I would like to put the easy problems earlier in the problem set
problems.sort(key=time_to_solve)
open("test_data.py", "w").write("test_data = " + str(problems))
