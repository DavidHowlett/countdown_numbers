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

Performance history:
 - First time it ran it took 118 ms to solve Ed's example problem
 - Added 100 tests
 100 puzzles attempted in 64433.9 milliseconds but 11 didn't solve
 - Added proper handling of duplicate numbers
 100 puzzles finished in 178299.0 milliseconds
 I note that the total solve time is entirely dominated by a very small number of tricky problems
 - regenerated the problem set in sorted order, and got a really hard one. I want to keep this problem set long term.
 100 puzzles finished in 385478.2 milliseconds
 - switched data structure to better deduplicate formula fragments with the same totals
 100 puzzles finished in 4953.9 milliseconds
 - changed from problems having 7 numbers like in Ed's example to 6 numbers like countdown
 100 puzzles finished in 2355.3 milliseconds


"""
import copy
import itertools
import time

from test_data import test_data


def solve(problem):
    initial_numbers, target = problem
    main_data_structure = make_main_data_structure(initial_numbers)

    # go faster: make the main loop generate all the fragments with len 2 then len 3 then len 4,
    # this will eliminate some reasons for the exact same fragment being generated more than once
    for _ in range(len(initial_numbers) - 1):
        previous_main_data_structure = copy.deepcopy(main_data_structure)
        for (
            used_numbers1,
            totals_and_fragments1,
        ) in previous_main_data_structure.items():
            # go faster: the below line does twice as many checks as needed.
            for (
                used_numbers2,
                totals_and_fragments2,
            ) in previous_main_data_structure.items():
                # if the two sets of numbers used overlap then generating a valid formula fragment is impossible,
                # so we should bail out early
                if used_numbers1 & used_numbers2:
                    continue
                # the set of numbers used in the new formula fragment will be the union of the
                # sets of numbers used in the two formula fragments used to make it up.
                new_used_numbers = used_numbers1 | used_numbers2
                new_totals_and_fragments = main_data_structure[new_used_numbers]
                for total1, formula_fragment1 in totals_and_fragments1.items():
                    for total2, formula_fragment2 in totals_and_fragments2.items():
                        # multiply -----------------------------
                        new_total = total1 * total2
                        if new_total not in new_totals_and_fragments:
                            new_formula_fragment = (
                                formula_fragment1,
                                "*",
                                formula_fragment2,
                            )
                            new_totals_and_fragments[new_total] = new_formula_fragment
                            if new_total == target:
                                return new_formula_fragment
                        # add ----------------------------------
                        new_total = total1 + total2
                        if new_total not in new_totals_and_fragments:
                            new_formula_fragment = (
                                formula_fragment1,
                                "+",
                                formula_fragment2,
                            )
                            new_totals_and_fragments[new_total] = new_formula_fragment
                            if new_total == target:
                                return new_formula_fragment
                        # subtract -----------------------------
                        new_total = total1 - total2
                        if new_total not in new_totals_and_fragments:
                            new_formula_fragment = (
                                formula_fragment1,
                                "-",
                                formula_fragment2,
                            )
                            new_totals_and_fragments[new_total] = new_formula_fragment
                            if new_total == target:
                                return new_formula_fragment
                        # divide -------------------------------
                        if (
                            total2 and not total1 % total2
                        ):  # divide by 0 is bad and decimals are never useful
                            new_total = total1 // total2
                            if new_total not in new_totals_and_fragments:
                                new_formula_fragment = (
                                    formula_fragment1,
                                    "/",
                                    formula_fragment2,
                                )
                                new_totals_and_fragments[
                                    new_total
                                ] = new_formula_fragment
                                if new_total == target:
                                    return new_formula_fragment


def make_main_data_structure(initial_numbers):
    initial_numbers_as_strings = []
    for number in initial_numbers:
        number_as_string = str(number)
        # to enable duplicate numbers in sets I add a space to end of the string representation of the duplicate number
        # to make it unique without changing its value
        while number_as_string in initial_numbers_as_strings:
            number_as_string += " "
        initial_numbers_as_strings.append(number_as_string)
    assert len(initial_numbers) == len(initial_numbers_as_strings)
    all_combinations_of_initial_numbers = list(
        itertools.chain.from_iterable(
            itertools.combinations(initial_numbers_as_strings, r)
            for r in range(1, len(initial_numbers_as_strings) + 1)
        )
    )
    # I want to initialise the main data structure to have every set of possible numbers that could be used in a formula
    # fragment
    main_data_structure = {
        frozenset(combo): {} for combo in all_combinations_of_initial_numbers
    }
    # I then add in all the starting numbers to act as the seed for the recursive filling of the main data structure
    # to come. The initial numbers are used to fill up the part of the data structure where the formula
    # would normally be
    for number in initial_numbers_as_strings:
        main_data_structure[frozenset([number])][int(number)] = int(number)
    # print(*(main_data_structure.items()), sep="\n")
    return main_data_structure


def solution_to_string(almost_formula):
    return str(almost_formula).replace("'", "").replace(",", "")


if __name__ == "__main__":
    start_time = time.perf_counter()
    for _problem in test_data:
        problem_start_time = time.perf_counter()
        print(*_problem)
        solution = solve(_problem)
        formula = solution_to_string(solution)
        print(formula)
        _target = _problem[1]
        # this is the main sanity check in the program
        assert eval(formula) == _target
        print(
            f"Problem took {((time.perf_counter() - problem_start_time)*1000):.1f} milliseconds"
        )
    print(
        f"{len(test_data)} puzzles finished in {((time.perf_counter() - start_time)*1000):.1f} milliseconds"
    )
    # the whole data structure
    # print(*(main_data_structure.items()), sep="\n")
    # What were the combos found?
    # print(main_data_structure[frozenset(initial_numbers)])
    # How many combos were found?
    # print(len(main_data_structure[frozenset(initial_numbers)]))
