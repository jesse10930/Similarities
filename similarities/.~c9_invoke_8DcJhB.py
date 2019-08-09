def lines(a, b):
    """Return lines in both a and b"""
    #initialize start of line variable to 0 and an empty list for the lines from a
    start_of_line = 0
    a_lines = []

    #iterate through loop until end of file reached
    while True:
        #finds location of first '\n' after the location of star_of_line, the end of the current line
        end_of_line = a.find('\n', start_of_line)
        #leaves loop if end of file reached
        if end_of_line < 0:
            break
        line = a[start_of_line:end_of_line]
        a_lines.append(line)
        start_of_line = end_of_line + 1

    start_of_line = 0
    b_lines = []
    while True:
        end_of_line = b.find('\n', start_of_line)
        if end_of_line < 0:
            break
        line = b[start_of_line:end_of_line]
        b_lines.append(line)
        start_of_line = end_of_line + 1

    same_lines = []
    for line_a in a_lines:
        for line_b in b_lines:
            if line_a == line_b:
                if line_a in same_lines:
                    continue
                else:
                    same_lines.append(line_a)

    return same_lines




    # TODO
    return []


def sentences(a, b):
    """Return sentences in both a and b"""

    # TODO
    return []


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    # TODO
    return []
