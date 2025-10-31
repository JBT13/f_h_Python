FILE_PATH_PREFIX = "/src/"
TABLE = "-"
ACTION_SHOW_CONSTITUENCIES = 1
ACTION_SHOW_PARTIES = 2
ACTION_SHOW_RESULTS = 3
ACTION_QUIT = 9
CONSTITUENCY_SIZE = 30
PARTY_SIZE = 32
RESULT_SIZE = 56

def main():
    """
    This function controls the main menu 
    (constituencies, parties, results) 
    """
    constituencies = None
    parties = None
    results = None

    action = 0

    while action != ACTION_QUIT:
        show_menu()
        action = get_action()

        if action == ACTION_SHOW_CONSTITUENCIES:
            constituencies = handle_constituencies_action(constituencies)
        elif action == ACTION_SHOW_PARTIES:
            parties = handle_parties_action(parties)
        elif action == ACTION_SHOW_RESULTS:
            results = handle_results_action(results, constituencies, parties)
        elif action == ACTION_QUIT:
            return 


def show_menu():
    print()
    print("1. Show constituencies")
    print("2. Show parties")
    print("3. Show results")
    print("9. Quit")
    print()


def get_action():
    """
    Returns:
        int: A valid integer action, or 0 if input is invalid.
    """
    try:
        action_input = input("Select an action: ")
        if not action_input:  
            return 0 
        return int(action_input)
    except ValueError:
        return 0 


def read_file_lines(file_name):
    """
    Returns:
        list: A list of strings, one for each line in the file.
        None: If the file is not found or is a directory.
    """
    try:
        with open(FILE_PATH_PREFIX + file_name, "r") as file:
            return file.readlines() 
    except (FileNotFoundError, IsADirectoryError):
        return None 


def handle_constituencies_action(current_constituencies):
    """
    Args:
        (dict or None)

    Returns:
        dict or None: The (potentially new) constituency data, or the
                      original data if loading failed.
    """
    data_to_print = current_constituencies

    if data_to_print is None:
        # attempt to load
        data_to_print = load_constituencies()

    if data_to_print:
        # Data is loaded (before or now) so we print it
        print_constituencies(data_to_print)

    # Return the loaded data (or None)
    return data_to_print


def load_constituencies():
    """
    File format expected: ConstituencyName;VoterCount

    Returns:
        dict: A dictionary mapping constituency names (str) to
              electoral counts (int). Returns None if file reading
              failed.
    """
    file_name = input("File name: ")
    lines = read_file_lines(file_name)

    if lines is None:
        return None

    constituencies = {}
    for line in lines: 
        parts = line.strip().split(";")
        if len(parts) == 2:
            name, voters = parts
            # Store in dict
            constituencies[name.strip()] = int(voters)

    return constituencies


def print_constituencies(constituencies):
    """
    Args:
        constituencies (dict): A dictionary of constituency data.
    """
    print()
    print("Constituency        Electorals")
    print(TABLE * CONSTITUENCY_SIZE)
    total = 0
    # Getting the values of the dict and printing it 
    for name, voters in constituencies.items():
        print(f"{name:<20}{voters:>10}")
        total += voters
    print(TABLE * CONSTITUENCY_SIZE) 
    print(f"{'Total:':<20}{total:>10}")


def handle_parties_action(current_parties):
    """
    Args:
        current_parties (dict or None): The cached data, or None.

    Returns:
        dict or None: The (potentially new) party data, or the
                      original data if loading failed.
    """
    data_to_print = current_parties

    if data_to_print is None:
        data_to_print = load_parties()

    if data_to_print:
        print_parties(data_to_print)

    return data_to_print


def load_parties():
    """
    File format expected: ListLetter;PartyName

    Returns:
        dict: A dictionary mapping party letters (str) to
              party names (str). Returns None if file reading
              failed.
    """
    file_name = input("File name: ")
    lines = read_file_lines(file_name)

    if lines is None:
        return None

    parties = {}
    for line in lines:
        parts = line.strip().split(";")
        if len(parts) == 2:
            letter, name = parts
            parties[letter.strip()] = name.strip()

    return parties


def print_parties(parties):
    """
    Args:
        parties (dict): A dictionary of party data.
    """
    print()
    print("List                       Party")
    print(TABLE * PARTY_SIZE)
    for letter, name in parties.items():
        print(f"{letter:<6}{name:>26}")


def handle_results_action(current_results, constituencies, parties):
    """
    Args:
        current_results (dict or None)
        constituencies (dict or None)
        parties (dict or None)

    Returns:
        dict or None: The (potentially new) results data, or the
                      original data if dependencies are not met
                      or loading failed.
    """
    if constituencies is None or parties is None:

        # Þessi input er hér bara for the love of the GAME
        random_kattis_input = input("File name for results: ")
        return current_results 

    results_to_use = current_results

    if results_to_use is None:
        results_to_use = load_results()

    if not results_to_use:
        return results_to_use

    const_name = input("Constituency: ").strip()

    # If constituency not found, just return (preserves loaded "results")
    if const_name not in results_to_use:
        return results_to_use

    # All is valid, print the formatted report
    print_single_constituency_result(
        const_name, results_to_use, constituencies, parties
    )

    return results_to_use


def load_results():
    """
    File format expected:
    ConstituencyName1
    ListLetterA;Votes
    ListLetterB;Votes

    Returns:
        dict: A dictionary mapping constituency names (str) to
              a list of (letter, votes) tuples. Returns None
              if file reading failed.
    """
    file_name = input("File name for results: ")
    lines = read_file_lines(file_name)

    if lines is None:
        return None

    results = {}
    current_const = None
    for line in lines:  
        line = line.strip()
        if not line:
            continue  
        if ";" not in line:
            # This line is a new constituency name
            current_const = line
            # preserves insertion order
            results[current_const] = []
        else:
            # This line is a vote count
            if current_const is not None:
                parts = line.split(";")
                if len(parts) == 2:  # Ensure valid vote line
                    letter, votes = parts
                    results[current_const].append(
                        (letter.strip(), int(votes))
                    )
    return results


def print_single_constituency_result(
        const_name, results, constituencies, parties):
    """
    Prints formatted constituency
    Calculates and displays votes, ratios, total, and turnout.

    Args:
        const_name (str): The name of the constituency to print.
        results (dict): The loaded results data.
        constituencies (dict): The loaded constituency data.
        parties (dict): The loaded party data.
    """
    print()
    print(f"{const_name}")
    print(f"{'List':<10}{'Party':>26}{'Votes':>10}{'Ratio':>10}")
    print(TABLE * RESULT_SIZE)

    try:
        current_votes = results[const_name]
    except KeyError:
        # Þetta hér er bara for the love of try and error
        return

    total_votes = sum(votes for _, votes in current_votes)

    for letter, votes in current_votes:
        party_name = parties.get(letter, "Unknown") # if letter not found == "Unknown"
        ratio = (votes / total_votes) * 100 if total_votes else 0 # safe division check (0/0) if total_votes == 0
        print(f"{letter:<10}{party_name:>26}{votes:>10}{ratio:>10.1f}")

    print(TABLE * RESULT_SIZE)
    print(f"{'Total:':<36}{total_votes:>10}{100.0:>10.1f}")

    voters = constituencies.get(const_name, 0) # if no const_name == 0
    turnout = (total_votes / voters) * 100 if voters else 0 # safe division check (0/0) if voters == 0
    print(f"{'Turnout:':<46}{turnout:>10.1f}")

if __name__ == "__main__":
    main()