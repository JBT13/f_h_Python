def is_float(string_to_test):
    try:
        float(string_to_test)
        return True
    except ValueError:
        return False
    
