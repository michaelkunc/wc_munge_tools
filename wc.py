
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
    lines = [l.replace(character, "") for l in user_list]
    return lines


def smaller(first_list, second_list):
    return len(first_list) > second_list
