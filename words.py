#def print_upper_words(string):
    #for i in string:
        #print(i.upper())

#def print_upper_words(string):

    #for i in string:
      #  if i.startswith('e'):
     #       print(i.upper())

def print_upper_words(string, must_start_with):
    """this function accept a list of string and a set of characters
    and returns the strings in the list that start with one of these characters
    """
    for i in string:
        if i.startswith(next(iter(must_start_with))):
            print(i.upper())

#print_upper_words(["hello", "hey", "goodbye", "yo", "yes","echo"])

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
