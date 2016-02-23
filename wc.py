#sql constants to remove from statements. 
#Note these are for the Oracle SQL dialect

SET_OPERATORS = ['UNION','UNION ALL', 'INTERSECT', 'MINUS']
ARITHMETIC_OPERATORS = ['+','-','/','*']
CHARACTER_OPERATORS =['||']
COMPARISON_OPERATORS = ['=', '!=', '^=', '<>', '>','<', '<=', '>=','IN','ANY',
['NOT', 'NOT IN', 'EXISTS']
LOGICAL_OPERATORS = ['NOT', 'AND','OR']

ALL_OPERATORS = SET_OPERATORS + ARITHMETIC_OPERATORS + CHARACTER_OPERATORS + COMPARISON_OPERATORS +
LOGICAL_OPERATORS

def open_and_split(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        return lines

#this should really be somethig like 'filter lines' with maybe different 
#keyworkds for 'include' and 'exclude'
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

#this now seems to be working
def remove_excess_whitespace(user_list):
    return [' '.join(l.split()) for l in user_list]

#e.g. to combine "United States" to "UnitedStates"
def combine_words(user_list, word):
    combined_word = word.replace(" ","")
    return replace_substring(user_list, word, combined_word)

#finds all lines that include a given substring and returns the count
def find_and_count(user_list, substring):
    lines = remove_lines(user_list, substring, 'include')
    return len(lines)
    

#remove an array of characters
def remove_substring_set(user_list, substring_set):
    for s in substring_set:
        user_list = remove_substring(user_list, s)
    return user_list

#this is a little broken
def save_list_file(user_list, write_path):
    with open(write_path, 'w') as f:
        for u in user_list:
            f.write(u)
