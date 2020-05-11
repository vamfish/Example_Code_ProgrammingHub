import os

try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'Presidency.txt'
    f = open(filename, 'r')
    text = f.read()
    f.close()
# Control jumps directly to here if
# any of the above lines throw IOError.
except IOError:
    # print(os.error) will <class 'OSError'>
    print('Problem reading:' + filename)

# In any case, the code then continues with
# the line after the try/except
