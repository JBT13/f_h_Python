def interleave_files_robust():
    try:
        # Get filenames safely
        file_a_name = input()
        file_b_name = input()

        with open(file_a_name, 'r') as file1, \
             open(file_b_name, 'r') as file2:
            
            # zip pairs lines until the shortest file ends
            for line_1, line_2 in zip(file1, file2):
                print(line_1.strip())
                print(line_2.strip())
    except:
        return

if __name__ == "__main__":
    interleave_files_robust()