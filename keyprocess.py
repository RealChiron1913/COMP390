def process_permutation(number_strings):
    return ''.join([str(int(char)-1) for char in number_strings])

def process_caesar(number_strings):
    return int(number_strings)

def process_other(number_strings):
    number_strings = ''.join([str(ord(char)) if char.isalpha() else char for char in number_strings])
    number_strings = str(int(number_strings)*int(number_strings)*len(number_strings))
    return number_strings

def remove_duplicates(number_strings):
    appeared = set()
    unique = []
    for number in number_strings:
        if number not in appeared:
            unique.append(number)
            appeared.add(number)
    return unique

def sort_and_index(number_strings):
    numbers = [int(s) for s in number_strings]
    sorted_numbers = sorted(numbers)
    processed = []
    for number in number_strings:
        index = sorted_numbers.index(int(number))
        processed.append(index)
    return processed

def key_process(number_strings, method, keyprocess=False):
    if method=='permutation' and not keyprocess:
        number_strings = process_permutation(number_strings)
    elif method=='caesar' and not keyprocess:
        return process_caesar(number_strings)
    else:
        number_strings = process_other(number_strings)
        if method=='caesar':
            return int(number_strings)

    number_strings = remove_duplicates(number_strings)
    processed = sort_and_index(number_strings)
    processed = ''.join([str(i) for i in processed])
    return processed