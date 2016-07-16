
names = ['jordan', 'kyle', 'kathy', 'brian']

def build_value_to_name_dict(names):
    values_to_names = {}
    for name in names:
        name_value = assign_value_to_a_name(name)
        if name_value in values_to_names:
            values_to_names[name_value].append(name)
        if name_value not in values_to_names:
            values_to_names[name_value] = [name]

    return values_to_names

def assign_value_to_a_name(name):
    name_value = 0
    for letter in name:
        # could also make a dict of letters:values and query that
        letter_value = ord(letter) - 96
        name_value += letter_value
    return name_value


def decide_tiebreak(names):
    names.sort(reverse = True)
    return names


def get_final_ordering(vals_to_names):
    final_ordering = []
    for val, names in iter(sorted(vals_to_names.iteritems(), reverse = True)):
        if len(names) > 1:
            names = decide_tiebreak(names)
        for name in names:
            final_ordering.append(name)
    return final_ordering


def answer(names):
    values_to_names = build_value_to_name_dict(names)
    final_ordering = get_final_ordering(values_to_names)
    print final_ordering
    return final_ordering


answer(names)
