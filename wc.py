
def open_and_split(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        return lines


def remove_lines(user_list, character, include_exclude):
    if include_exclude.lower() == 'include':
        lines = [l for l in user_list if character in l]
        return lines
    elif include_exclude.lower() == 'exclude':
        lines = [l for l in user_list if character not in l]
        return lines
    else:
        raise ValueError(
            "Please enter 'include' or 'exclude' for the final argument")


def clear_empty_lines(user_list):
    return filter(None, user_list)

def remove_substring(user_list, character):
    return  [l.replace(character, "") for l in user_list]

def replace_substring(user_list, old_character, new_character):
    return [l.replace(old_character, new_character) for l in user_list]

def smaller(first_list, second_list):
    return len(first_list) > len(second_list)

def replace_single_substring(user_list, index, old_character, new_character):
    return user_list[index].replace(old_character, new_character)

#need to test this method
def remove_excess_whitespace(user_list):
    return [' '.join(l.split()) for l in list]