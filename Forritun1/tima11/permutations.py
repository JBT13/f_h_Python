def main():
    a = input()
    b = input()
    if are_permutation_of_same_digits(a, b):
        print(f"The numbers {a} and {b} are permutations of each other.")
    else:
        print(f"The numbers {a} and {b} are not permutations of each other.")


def are_permutation_of_same_digits(m: str, n: str) -> bool:
    return sorted(str(m)) == sorted(str(n))
main()