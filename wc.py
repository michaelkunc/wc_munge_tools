def test_the_tests():
	return 'is this thing on?'

def open_and_split(filepath):
	with open(filepath) as f:
		lines = f.read().splitlines()
		return lines


def clean_lines(user_list, character, include_exclude):
	if include_exclude == 'include':
		lines = [l for l in user_list if character in l]
		return lines
	elif include_exclude == 'exclude':
		lines = [l for l in user_list if character not in l]
		return lines
	else:
		raise ValueError("Please enter 'include' or 'exclude' for the final argument")