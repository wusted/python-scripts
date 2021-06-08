#!/usr/bin/python3

def count(substr, theStr):
    # Initialize count and start to 0
    counter = 0
    start = 0

    # Search through the string till
    # we reach the end of it
    while start < len(theStr):

        # check if a substring is present from
        # "start" position till the end
        pos = theStr.find(substr, start)

        if pos != -1:
            # If a substring is present, move "start" to
            # the next position from start of the substring
            start = pos + 1
            counter += 1
        else:
            # If no further substring is present
            break
    # return the value of count
    return counter

# Driver code
string = "GeeksforGeeksforGeeksforGeeks"
print(count("GeeksforGeeks", string))