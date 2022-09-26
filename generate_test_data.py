"""
This generates the test data. Please don't re-run this without good cause.
"""

import random
import time

import main

top_row = [25, 50, 75, 100]
bottom_row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] * 2
all_numbers = top_row + bottom_row
problems = []


# In the below generator I limit myself to length 6 and check if each problem is solvable.
# It is possible to construct more difficult problems by generating problems of length 7.
while len(problems) < 100:
    problem = (random.sample(all_numbers, 6), random.randrange(100, 999))
    start_time = time.perf_counter()
    solution = main.solve(problem)
    solve_time = time.perf_counter() - start_time
    # this makes progress visible
    print(problem)
    print(main.solution_to_string(solution))
    if solution:
        problems.append((problem, solve_time))

# I put the easy problems earlier in the problem set so that debugging is done with trivial problems
problems.sort(key=lambda x: x[1])
problems = [x[0] for x in problems]
open("test_data.py", "w").write("test_data = " + str(problems))
