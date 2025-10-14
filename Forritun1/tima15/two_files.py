import itertools

def interleave_files_robust():
    try:
        # Get filenames safely
        file_a_name = input()
        file_b_name = input()

        with open("/src/" + file_a_name, 'r') as file1, \
             open("/src/" + file_b_name, 'r') as file2:
            
            # Interleave lines from both files, filling shorter file with None
            for line_1, line_2 in itertools.zip_longest(file1, file2, fillvalue=None):
                if line_1:  # Check if line from file 1 is not None
                    print(line_1.strip())
                if line_2:  # Check if line from file 2 is not None
                    print(line_2.strip())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    interleave_files_robust()



# import itertools

# def interleave_files_robust():
#     try:
#         # Get filenames safely
#         file_a_name = input()
#         file_b_name = input()

#         with open("/src/" + file_a_name, 'r') as file1, \
#              open("/src/" + file_b_name, 'r') as file2:
            
            
#             for line_1, line_2 in itertools.zip_longest(file1, file2, fileValue=None):
#                 print(line_1.strip())
#                 print(line_2.strip())

#     except:
#         return

# if __name__ == "__main__":
#     interleave_files_robust()

