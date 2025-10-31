def main():
    """Main program loop / Menu."""
    constituencies = None
    parties = None
    results = None
    action = 0

    while action != 9:
        print()
        print("1. Show constituencies")
        print("2. Show parties")
        print("3. Show results")
        print("9. Quit")
        print()

        try:
            action = int(input("Select an action: "))
        except ValueError:
            continue

        if action == 1:
            constituencies = show_constituencies(constituencies)
        elif action == 2:
            parties = show_parties(parties)
        elif action == 3:
            results = show_results(results, constituencies, parties)
        elif action == 9:
            return


def show_constituencies(constituencies):
    """Reads and prints constituency data, unless already loaded."""
    if constituencies is None:
        file_name = input("File name: ")
        try:
            with open(file_name, "r") as file:
                constituencies = {}
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) == 2:
                        name, voters = parts
                        constituencies[name.strip()] = int(voters)
        except FileNotFoundError:
            return constituencies

    if constituencies:
        print()
        print("Constituency        Electorals")
        print("------------------------------")
        total = 0
        for name, voters in constituencies.items():
            print(f"{name:<20}{voters:>10}")
            total += voters
        print("------------------------------")
        print(f"{'Total:':<20}{total:>10}")

    return constituencies


def show_parties(parties):
    """Reads and prints party data, unless already loaded."""
    if parties is None:
        file_name = input("File name: ")
        try:
            with open(file_name, "r") as file:
                parties = {}
                for line in file:
                    parts = line.strip().split(";")
                    if len(parts) == 2:
                        letter, name = parts
                        parties[letter.strip()] = name.strip()
        except FileNotFoundError:
            return parties

    if parties:
        print()
        print("List                       Party")
        print("--------------------------------")
        for letter, name in parties.items():
            print(f"{letter:<6}{name:>26}")

    return parties


def show_results(results, constituencies, parties):
    """Reads election results and shows data for a chosen constituency."""
    if constituencies is None or parties is None:
        name = input("File name for results: ")
        return results

    if results is None:
        file_name = input("File name for results: ")
        try:
            with open(file_name, "r") as file:
                results = {}
                current_const = None
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    if ";" not in line:
                        current_const = line
                        results[current_const] = []
                    else:
                        letter, votes = line.split(";")
                        results[current_const].append((letter.strip(), int(votes)))
        except FileNotFoundError:
            return results

    if not results:
        return results

    const_name = input("Constituency: ").strip()

    if const_name not in results:
        return results

    print()
    print(f"{const_name}")
    print(f"{'List':<10}{'Party':>26}{'Votes':>10}{'Ratio':>10}")
    print("--------------------------------------------------------")

    total_votes = sum(votes for _, votes in results[const_name])

    for letter, votes in results[const_name]:
        party_name = parties.get(letter, "Unknown")
        ratio = (votes / total_votes) * 100 if total_votes else 0
        print(f"{letter:<10}{party_name:>26}{votes:>10}{ratio:>10.1f}")

    print("--------------------------------------------------------")
    print(f"{'Total:':<36}{total_votes:>10}{100.0:>10.1f}")

    voters = constituencies.get(const_name, 0)
    turnout = (total_votes / voters) * 100 if voters else 0
    print(f"{'Turnout:':<46}{turnout:>10.1f}")

    return results


if __name__ == "__main__":
    main()
