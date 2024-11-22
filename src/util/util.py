def check_missing_input(arr_input):
    for input in arr_input:
        if input is None:
            return True
    return False