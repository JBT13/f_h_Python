from typing import List


# implement prime_sum(a_list) here below
def prime_sum(the_given_list_of_numbers: List[int]) -> int:
    """Returns the sum of all prime numbers from the list."""
    count = 0
    for number in the_given_list_of_numbers:
        if is_prime(number):
            count += number

    return count
    # Use list comprehension.
    # You should make use of the is_prime() function given below.


# This function is given, do not change it, you can however call it.
def is_prime(number_to_check: int) -> bool:
    """Returns True if the number n is prime, False otherwise."""

    if number_to_check < 2:
        return False

    potential_factor = 2
    while potential_factor**2 <= number_to_check:
        if number_to_check % potential_factor == 0:
            return False

        potential_factor += 1

    return True
