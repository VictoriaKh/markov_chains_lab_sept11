"""Generate Markov text from text files."""

from random import choice
import sys


def open_and_read_file():
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_path = sys.argv[1]
    string_file = open(file_path).read()

    return string_file




def make_chains(text_string,n_gram):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 


        'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    ######################################################
    # chains = {}
    # words = text_string.split()
    # for i in range(len(words)-2):
    #     key = (words[i], words[i + 1])
    #     if key in chains:
    #         chains[key].append(words[i + 2])
    #     else:
    #         chains[key]  = [words[i + 2]]   

    ####### further study #########

    chains = {}
    words = text_string.split()
    for i in range(len(words)-(n_gram)):
        key = words[i : (i + (n_gram))]  #list slicing is exclusive,hence we are doing(i+ n_gram)
        key = tuple(key)
        
        if key in chains:
            chains[key].append(words[i + n_gram])
        else:
            chains[key]  = [words[i + n_gram]]

     
  
    # your code goes here

    return chains


def make_text(chains,n_gram):
    """Return text from chains."""



    # words = []

    # # your code goes here
    # keys_of_dict = chains.keys()
    # lst = list(keys_of_dict)
       
    # first_random_key = choice(lst)
    # first_random_key = list(first_random_key)

    

    
    # words.append(first_random_key[0])
    # words.append(first_random_key[1])
    # while True:
    #     new_key = tuple(words[-2:])
    #     if new_key not in chains:
    #         break
    #     random_word_from_value = choice(chains[new_key])
    #     words.append(random_word_from_value)
    
   
   
    # return " ".join(words)


################### further study #############

    words = []

    # your code goes here
    keys_of_dict = chains.keys()
    lst = list(keys_of_dict)
       
    first_random_key = choice(lst)
    first_random_key = list(first_random_key)

    

    
    words.extend(first_random_key)
    while True:
        new_key = tuple(words[-n_gram:])
        if new_key not in chains:
            break
        random_word_from_value = choice(chains[new_key])
        words.append(random_word_from_value)
    
   
   
    return " ".join(words)

def main():  #using this function only for further study,to make n_gram global for code without using "global"
    n_gram = int(input("enter a number for n-gram >"))


    #input_path = "green-eggs.txt"    #file name can be used if 'sys' library is not imported

    # Open the file and turn it into one long string
    input_text = open_and_read_file()

    # Get a Markov chain
    chains = make_chains(input_text,n_gram)

    # Produce random text
    random_text = make_text(chains,n_gram)

    print(random_text)

main()        



