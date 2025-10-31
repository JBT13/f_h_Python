WIDTH_1 = 20
WIDTH_2 = 10
WIDTH_3 = 6
WIDTH_4 = 26
def constituencies():
    new_s = input("File name: ")
    dict_data = {}
    try:
        file = open(f"{new_s}", "r")
    except FileNotFoundError:
        return None
    for line in file:
        line = line.strip().split(";")
        dict_data[line[0]] = int(line[1])   
    return dict_data

def format_constituency(s): 
    print()
    print(f"{'Constituency':<{WIDTH_1}}{'Electorals':<{WIDTH_2}}")
    print("-" * 30)
    elect = 0
    for key, value in s.items():
        print(f"{key:<{WIDTH_1}}{value:>{WIDTH_2}}")
        elect += value
    print("-" * 30)
    print(f"{'Total:':<{WIDTH_1}}{elect:>{WIDTH_2}}")

def parties():
    new_2 = input("File name: ")
    try:
        file_name = open(f"{new_2}", "r")
    except FileNotFoundError:
        return None
    dict_parties = {}
    #par = ""
    for data in file_name:
        data = data.strip().split(";")
        dict_parties[data[0]] = str(data[1])
    return dict_parties

def format_parties(k):
    print()
    print(f"{'List':<{WIDTH_3}}{'Party':>{WIDTH_4}}")
    print("-" * 32)
    for key, value in k.items():
        print(f"{key:<{WIDTH_3}}{value:>{WIDTH_4}}")
    


def results():  #Verður að breyta í fallið í prufa, bilað eins og er 
    new_3 = input("File name for results: ")
    try:
        open_file = open(f"{new_3}", "r")
    except FileNotFoundError:
        return None
    dict_results = {}
    for party in open_file:
        party = party.strip().split(";")

        if len(party) == 1:
            constit = party[0]
            dict_results[constit] = []
        else: 
            dict_results[constit] += [(party[0], int(party[1]))]

    return dict_results

def format_result(s, con, parties):
    constit_input = input("Constituency: ")
    if constit_input not in s:
        return None
    print()
    print(constit_input)
    print(f"{'List':<{WIDTH_2}}{'Party':>{WIDTH_4}}{'Votes':>{WIDTH_2}}{'Ratio':>{WIDTH_2}}")
    print("-" * 56)
    total_votes = con[constit_input]
    ratio = s[constit_input]
    count = 0
    sum = 0 
    voters = 0
    for x in ratio:
        voters += x[1]
    for k in ratio:
        votes = k[1]
        count += votes
        party = parties[k[0]]
        main_ratio = 100 * votes/voters
        sum += main_ratio
        print(f"{k[0]:<{WIDTH_2}}{party:>{WIDTH_4}}{votes:>{WIDTH_2}}{main_ratio:>{WIDTH_2}.1f}")
    turnout = count/total_votes*100
    print("-" * 56)
    print(f"{'Total:':<{WIDTH_2}}{count:>{WIDTH_2 + WIDTH_4}}{sum:>{WIDTH_2}}")
    print(f"{'Turnout:':<{WIDTH_2}}{turnout:>{(WIDTH_2 *2) + WIDTH_4}.1f}")
    

def main():
    contstituency = None
    parties_file = None
    results_file = None
    s = "0"

    while s != "9":
        print()
        s = input(
        "1. Show constituencies\n"
        "2. Show parties\n"
        "3. Show results\n"
        "9. Quit\n"
        "\n"
        "Select an action: "
        )
         
        if s == "1":
            if contstituency is None:
                contstituency = constituencies()
                if contstituency is None:
                    continue
            format_constituency(contstituency) 
            
        elif s == "2":
            if parties_file is None:
                parties_file = parties()
                if parties_file is None:
                    continue
            format_parties(parties_file)

        elif s == "3":
            # Load results file if not already loaded or if the previous attempt failed
            if results_file is None:
                results_file = results()
                if results_file is None:
                    # If results loading failed, we stop here and prompt for the next action.
                    continue
               
            
            # Check for dependencies: constituencies and parties files must be loaded
            # before we can format the results.
            if contstituency is None and parties_file is None:
                
                random = input("Constituency: ")
                return 

            # Now all necessary data (results_file, contstituency, parties_file) should be loaded.
            # We can safely call format_result.
            if results_file is not None and contstituency is not None and parties_file is not None:
                format_result(results_file, contstituency, parties_file)
           

if __name__ == "__main__":
    main()