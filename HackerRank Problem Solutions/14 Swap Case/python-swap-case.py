def swap_case(s):
    char_list = list(s)
    for i in range(len(char_list)):
        if char_list[i].isupper():
            char_list[i] = char_list[i].lower()
        elif char_list[i].islower():
            char_list[i] = char_list[i].upper()
        else:
            pass

    return "".join(char_list)