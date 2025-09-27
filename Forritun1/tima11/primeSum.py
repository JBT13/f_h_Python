def prime_sum(list):
    
    prime_list = []
    for n in list:
        if is_prime(n):
            prime_list.append(n)

    return sum(prime_list)


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
