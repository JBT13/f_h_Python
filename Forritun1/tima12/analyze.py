def main():
    input_list = get_correct_data()

    sorted_list = sorted(input_list)
    composite = set()
    for i in input_list:
        if not is_prime(i):
            composite.add(i)

    composite_list = list(composite)
    sorted_composite_list = sorted(composite_list)

    min_number = min(input_list)
    max_number = max(input_list)
    avg_number = sum(input_list)/len(input_list)

    print(f"Input list: {input_list}")
    print(f"Sorted list: {sorted_list}")
    print(f"Composite list: {sorted_composite_list}")
    print(f"Min: {min_number}, Max: {max_number}, Average: {avg_number:.2f}")


def get_correct_data() -> list:
    """Asks user repeatedly for input until valid."""

    input_list = get_data()
    while input_list == None:
        input_list = get_data()
    
    return input_list


    raise NotImplementedError  # TODO: Finish this function.


def get_data():
    """Returns a list of positive integers input by the user.

    Returns None if the input contains non-integers or integers < 0.
    """
    positive = input().split(",")
    for i in positive:
        if i.isdigit():
            i = int(i)
        else:
            print("Incorrect input! Please try again.")
            return None
        
        if i < 0:
            print("Incorrect input! Please try again.")
            return None

    positive = list(map(int, positive))
    return positive

    raise NotImplementedError  # TODO: Implement this function


# Add as many functions as you think you could use.


def is_prime(n: int) -> bool:
    """Returns True if the given positive number is prime and False otherwise."""

    if n < 2:
        return False

    for i in range(2, n):  # Feel free to improve this function if you like.
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    main()

# def sorted_list(s):
    
# def composite_list(c):
    
# def min(l):

# def max(l):

# def avg(l):