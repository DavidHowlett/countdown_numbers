"""
I attempt to combine 6 numbers and the 4 basic arithmatic operations as quickly as possible

The main data structure is a collection of formula fragments. Each formula fragment must record:
    - a frozenset of the numbers used
    - total
    - (left_fragment, operator, right_fragment)
The frozenset is used to avoid generating formulas with duplicate numbers in.
The totals are used to avoid recalculating the whole formula each time a new formula is generated.
The left_fragment, operator and right fragment are used to reconstruct the whole formula at the end of the calculation.
They are also used to avoid recreating duplicate entries for ways to generating formulas

"""
import copy
import itertools
import time

start_time = time.perf_counter()
target = 673

initial_numbers = [1, 10, 100, 1000, 10000, 100000, 1000000]
initial_numbers = [1, 10, 100, 1000]
initial_numbers = [75, 6, 3, 4, 5, 10]
all_combinations_of_initial_numbers = list(
    itertools.chain.from_iterable(
        itertools.combinations(initial_numbers, r)
        for r in range(1, len(initial_numbers) + 1)
    )
)

# I want to initialise the main data structure to have every set of possible numbers that could be used in a formula
# fragment
main_data_structure = {
    frozenset(combo): set() for combo in all_combinations_of_initial_numbers
}
# I then add in all the starting numbers to act as the seed for the recursive filling of the main data structure to come
# The initial numbers are used to fill up the part of the data structure where the formula would normally be
for number in initial_numbers:
    main_data_structure[frozenset([number])].add((number, number))

# print(*(main_data_structure.items()), sep="\n")

# go faster: make the main loop generate all the fragments with len 2 then len 3 then len 4,
# this will eliminate some reasons for the exact same fragment being generated more than once
for _ in range(len(initial_numbers) - 1):
    previous_main_data_structure = copy.deepcopy(main_data_structure)
    for used_numbers1, fragment_set1 in previous_main_data_structure.items():
        # go faster: the below line does twice as many checks as needed.
        for used_numbers2, fragment_set2 in previous_main_data_structure.items():
            # if the two sets of numbers used overlap then generating a valid formula fragment is impossible,
            # so we should bail out early
            if used_numbers1 & used_numbers2:
                continue
            # the set of numbers used in the new formula fragment will be the union of the
            # sets of numbers used in the two formula fragments used to make it up.
            new_used_numbers = used_numbers1 | used_numbers2
            place_to_put_new_combos = main_data_structure[new_used_numbers]
            for total1, formula_fragment1 in fragment_set1:
                for total2, formula_fragment2 in fragment_set2:
                    # go faster: (most important) only add a formula fragment to the main datastructure iff the
                    # combination of new_used_numbers and new_total is unique. Repeats have no value.
                    # subtract --------------------------
                    new_total = total1 - total2
                    new_thing = (
                        new_total,
                        (formula_fragment1, "-", formula_fragment2),
                    )
                    if new_total == target:
                        print(new_thing)
                        print(f'puzzle finished in {(time.perf_counter() - start_time)*1000} ms')
                        exit()
                    # go faster: this "if" can be skipped by adding directly
                    if new_thing not in place_to_put_new_combos:
                        # print(f"combo {new_thing}")
                        place_to_put_new_combos.add(new_thing)
                    # divide ----------------------------
                    if total2 and not total1 % total2:  # decimals are never useful
                        new_total = total1 // total2
                        new_thing = (
                            new_total,
                            (formula_fragment1, "/", formula_fragment2),
                        )
                        if new_total == target:
                            print(new_thing)
                            print(f'puzzle finished in {(time.perf_counter() - start_time)*1000} ms')
                            exit()
                        # go faster: this "if" can be skipped by adding directly
                        if new_thing not in place_to_put_new_combos:
                            # print(f"combo {new_thing}")
                            place_to_put_new_combos.add(new_thing)
                    # plus -------------------------------
                    new_total = total1 + total2
                    new_thing = (
                        new_total,
                        (formula_fragment1, "+", formula_fragment2),
                    )
                    new_thing_permutation = (
                        total1 + total2,
                        (formula_fragment2, "+", formula_fragment1),
                    )
                    if new_total == target:
                        print(new_thing)
                        print(f'puzzle finished in {(time.perf_counter() - start_time)*1000} ms')
                        exit()
                    if (
                        new_thing not in place_to_put_new_combos
                        and new_thing_permutation not in place_to_put_new_combos
                    ):
                        # print(f"combo {new_thing}")
                        place_to_put_new_combos.add(new_thing)
                    # multiply --------------------------
                    new_total = total1 * total2
                    new_thing = (
                        new_total,
                        (formula_fragment1, "*", formula_fragment2),
                    )
                    new_thing_permutation = (
                        total1 * total2,
                        (formula_fragment2, "*", formula_fragment1),
                    )
                    if new_total == target:
                        print(new_thing)
                        print(f'puzzle finished in {(time.perf_counter() - start_time)*1000} ms')
                        exit()
                    if (
                        new_thing not in place_to_put_new_combos
                        and new_thing_permutation not in place_to_put_new_combos
                    ):
                        # print(f"combo {new_thing}")
                        place_to_put_new_combos.add(new_thing)


# the whole data structure
# print(*(main_data_structure.items()), sep="\n")
# What were the combos found?
# print(main_data_structure[frozenset(initial_numbers)])
# How many combos were found?
# print(len(main_data_structure[frozenset(initial_numbers)]))
