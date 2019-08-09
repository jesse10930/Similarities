def lines(a, b):
    """Return lines in both a and b"""
    #initialize start of line variable to 0 and an empty list for the lines from a
    start_of_line = 0
    a_lines = []

    #iterate through loop until end of file reached
    while True:

        #finds location of first '\n' after the location of star_of_line, the end of the current line
        end_of_line = a.find('\n', start_of_line)

        #leaves loop if end of file reached after saving last line to list
        if end_of_line < 0:
            line = a[start_of_line:]
            a_lines.append(line)
            break

        #stores line from a into a variable, then puts that variable into a list
        line = a[start_of_line:end_of_line]
        a_lines.append(line)

        #set start_of_line to position after the last '\n'
        start_of_line = end_of_line + 1


    #initialize start of line variable to 0 and en empty list for the lines from b
    start_of_line = 0
    b_lines = []

    #iterate through loop until end of file reached
    while True:

        #finds location of first '\n' after the location of start_of_line, the end of the current line
        end_of_line = b.find('\n', start_of_line)

        #leaves loop if end of file reached after saving last line to list
        if end_of_line < 0:
            line = b[start_of_line:]
            b_lines.append(line)
            break

        #stores line from b into a variable, then puts that variable into a list
        line = b[start_of_line:end_of_line]
        b_lines.append(line)

        #set start_of_line to position after the last '\n'
        start_of_line = end_of_line + 1


    #initialize empty list
    same_lines = []

    #iterate through list a, iterate through list b, if two elements are the same, store into a new list, if unique
    for line_a in a_lines:
        for line_b in b_lines:
            if line_a == line_b:
                if line_a in same_lines:
                    continue
                else:
                    same_lines.append(line_a)

    # TODO
    return same_lines

def sentences(a, b):
    """Return sentences in both a and b"""
    #import sent_tokenize, then store sentences from a in a list and sentences from b in a list
    from nltk.tokenize import sent_tokenize
    a_sentences = sent_tokenize(a)
    b_sentences = sent_tokenize(b)

    #initialize same_sentences as empty list, iterate through sentences from a, iterate through sentences from b, if two sentences match, store in same sentences list if unique
    same_sentences = []
    for sent_a in a_sentences:
        for sent_b in b_sentences:
            if sent_a == sent_b:
                if sent_a in same_sentences:
                    continue
                else:
                    same_sentences.append(sent_a)

    # TODO
    return same_sentences


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    #procedure to make list of substrings of length n
    def list_of_substrings(text_input, sub_len):

        #initializing a list and two integer variables for iteration
        subs = []
        start = 0
        end = sub_len

        #loops through text until substring shorter than n
        while True:

            #storing substring of size n and checkint to make sure it is at last n chars long
            substring = text_input[start:end]
            if len(substring) < sub_len:
                break

            #appending the current substring to the subs list, moving start/end counters one spot to the right
            subs.append(substring)
            start = start + 1
            end = end + 1

        #returns the subs list to main
        return subs

    #procedure to find common substrings between two lists
    def compare_lists(list_a, list_b):

        #initializing a list for common substrings
        same = []

        #iterate through list a, iterate through list b, if substrings are equal, store in same list, if unique
        for sub_a in list_a:
            for sub_b in list_b:
                if sub_a == sub_b:
                    if sub_a in same:
                        continue
                    else:
                        same.append(sub_a)

        #returns the same list to main
        return same

    #runs procs on input text files
    a_substrings = list_of_substrings(a, n)
    b_substrings = list_of_substrings(b, n)
    same_substrings = compare_lists(a_substrings, b_substrings)

    # TODO
    return same_substrings