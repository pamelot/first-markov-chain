import sys, random
from time import sleep

filename = str(sys.argv[1])
def make_chains(file_path):
    """Takes input text as string; returns dictionary of markov chains."""
    
    complete_string = ''
    tuple_dictionary = {}
    with open(filename) as source_file:
        for line in source_file:
            complete_string = complete_string + line.rstrip() + ' '
    complete_list = complete_string.split(" ") 
    
    for i in range(len(complete_list)-2):
        new_tuple = (complete_list[i], complete_list[i +1])

        if new_tuple in tuple_dictionary:
            tuple_dictionary[new_tuple].append(complete_list[i+2])
        else:
            tuple_dictionary[new_tuple] = [complete_list[i+2]]
        #alternatively, we can use setdefault() method as shown below   
        #tuple_dictionary.setdefault(new_tuple, []).append(complete_list[i+2])

    return tuple_dictionary

  

make_chains(filename)


def make_text():
    """Takes dictionary of markov chains; returns random text."""

    pair_dictionary = make_chains(filename)
    current_tuple = random.choice(pair_dictionary.keys())
    output_list = list(current_tuple)

    while current_tuple in pair_dictionary:
        next_word = random.choice(pair_dictionary[current_tuple])
        output_list.append(next_word)
        current_tuple = (current_tuple[1], next_word)
    else:
        output_list_as_string = " ".join(output_list)
        output_list_as_string = output_list_as_string[0].upper() + output_list_as_string[1:]
        print output_list_as_string


make_text()

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "Some text"

# # Get a Markov chain
# chain_dict = make_chains(input_text)

# # Produce random text
# random_text = make_text(chain_dict)

# print random_text
