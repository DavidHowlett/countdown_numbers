"""
I attempt to combine 6 numbers and the 4 basic arithmatic operations to make a random three-digit number as fast as
possible.

The main data structure is a collection of formula fragments. Each formula fragment must record:
    - a frozenset of the numbers used
    - the total reached by evaluating the formula fragment
    - the formula itself. This is normally a tuple of (left_fragment, operator, right_fragment) but it can also be an
    integer for the base numbers.
The frozenset is used to avoid generating formulas with duplicate numbers in.
The totals are used to avoid recalculating the whole formula each time a new formula is generated.
The left_fragment, operator and right fragment are used to reconstruct the whole formula at the end of the calculation.

In the final code below the whole program revolves around a complex, nested datastructure that allows the skipping of
most of the calculation without loss of any possible solutions.

Performance history:
 - First time it ran it took 118 ms to solve Ed's example problem
 - Added 100 tests
 100 puzzles attempted in 64433.9 milliseconds but 11 didn't solve
 - Added proper handling of duplicate numbers
 100 puzzles finished in 178299.0 milliseconds
 I note that the total solve time is entirely dominated by a very small number of tricky problems
 - regenerated the problem set in sorted order, and got a really hard one.
 100 puzzles finished in 385478.2 milliseconds
 - switched data structure to better deduplicate formula fragments with the same totals
 100 puzzles finished in 4953.9 milliseconds
 - changed from problems having 7 numbers like in Ed's example to 6 numbers like in original countdown
 100 puzzles finished in 2355.3 milliseconds
 - I generated the formula fragments in size order
 100 puzzles finished in 406.4 milliseconds


"""
import itertools
import time

from test_data import test_data


def solve(problem):
    initial_numbers, target = problem
    main_data_structure = make_main_data_structure(initial_numbers)
    for fragment_len_to_make in range(2, len(initial_numbers) + 1):
        # I choose to start with the big fragments on the left and the small fragments on the right.
        # This often makes the solutions found easy to read.
        # I can in theory make things go faster by testing fewer of the left_fragment_lengths for add and multiply
        # as those operations are commutative. After looking at a+b there is not point looking at b+a. However, the
        # approach I initially tried increased runtime by about 7% due to the extra overhead of the extra outer loops.
        for left_fragment_length in range(fragment_len_to_make - 1, 0, -1):
            # the left and right fragments should in total have the desired length
            right_fragment_length = fragment_len_to_make - left_fragment_length
            for (used_numbers1, totals_and_fragments1) in main_data_structure[left_fragment_length].items():
                for (used_numbers2, totals_and_fragments2) in main_data_structure[right_fragment_length].items():
                    # if the two sets of numbers used overlap then generating a valid formula fragment is impossible,
                    # so we should bail out early
                    if used_numbers1 & used_numbers2:
                        continue
                    # the set of numbers used in the new formula fragment will be the union of the
                    # sets of numbers used in the two formula fragments used to make it up.
                    new_used_numbers = used_numbers1 | used_numbers2
                    new_totals_and_fragments = main_data_structure[fragment_len_to_make][new_used_numbers]
                    for total1, formula_fragment1 in totals_and_fragments1.items():
                        for total2, formula_fragment2 in totals_and_fragments2.items():
                            # multiply -----------------------------
                            new_total = total1 * total2
                            if new_total not in new_totals_and_fragments or new_total == target:
                                new_formula_fragment = (
                                    formula_fragment1,
                                    "*",
                                    formula_fragment2,
                                )
                                new_totals_and_fragments[new_total] = new_formula_fragment
                                if new_total == target:
                                    yield new_formula_fragment
                            # add ----------------------------------
                            new_total = total1 + total2
                            if new_total not in new_totals_and_fragments or new_total == target:
                                new_formula_fragment = (
                                    formula_fragment1,
                                    "+",
                                    formula_fragment2,
                                )
                                new_totals_and_fragments[new_total] = new_formula_fragment
                                if new_total == target:
                                    yield new_formula_fragment
                            # subtract -----------------------------
                            new_total = total1 - total2
                            if new_total not in new_totals_and_fragments or new_total == target:
                                new_formula_fragment = (
                                    formula_fragment1,
                                    "-",
                                    formula_fragment2,
                                )
                                new_totals_and_fragments[new_total] = new_formula_fragment
                                if new_total == target:
                                    yield new_formula_fragment
                            # divide -------------------------------
                            if total2 and not total1 % total2:  # divide by 0 is bad and decimals are never useful
                                new_total = total1 // total2
                                if new_total not in new_totals_and_fragments or new_total == target:
                                    new_formula_fragment = (
                                        formula_fragment1,
                                        "/",
                                        formula_fragment2,
                                    )
                                    new_totals_and_fragments[new_total] = new_formula_fragment
                                    if new_total == target:
                                        yield new_formula_fragment
    print('foo')


def make_main_data_structure(initial_numbers):
    initial_number_len = len(initial_numbers)
    initial_numbers_as_strings = []
    for number in initial_numbers:
        number_as_string = str(number)
        # to enable duplicate numbers in sets I add spaces to end of the string representation of the duplicate numbers
        # to make them unique without changing their value
        while number_as_string in initial_numbers_as_strings:
            number_as_string += " "
        initial_numbers_as_strings.append(number_as_string)
    assert initial_number_len == len(initial_numbers_as_strings)
    all_combinations_of_initial_numbers = itertools.chain.from_iterable(
        itertools.combinations(initial_numbers_as_strings, r) for r in range(1, initial_number_len + 1)
    )

    # I want to initialise the main data structure to have every set of possible numbers that could be used in a formula
    # fragment and I want to group them by length
    main_data_structure = [{} for _ in range(initial_number_len + 1)]
    for combo in all_combinations_of_initial_numbers:
        main_data_structure[len(combo)][frozenset(combo)] = {}

    # I then add in all the starting numbers. They sum to themselves, are represented by themselves in a formula and
    # only use themselves for representation. These three properties mean they appear in the below formula three times.
    # More specifically the initial numbers are used to fill up the parts of the data structure where the formula
    # fragment and the total would normally be
    for number in initial_numbers_as_strings:
        main_data_structure[1][frozenset([number])][int(number)] = int(number)
    # print(*(main_data_structure.items()), sep="\n")
    return main_data_structure


def solution_to_string(almost_formula):
    return str(almost_formula).replace("'", "").replace(",", "")


if __name__ == "__main__":
    problem_start_time = time.perf_counter()
    for solution in solve(([25,50,75,100,3,6],952)):
        print(solution_to_string(solution))
    print(f"Problem took {((time.perf_counter() - problem_start_time)*1000):.2f} milliseconds")
