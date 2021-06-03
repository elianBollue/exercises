import sys

with open(sys.argv[1]) as file:
    with open(sys.argv[2], 'w') as copy:
        copy.write(file.read())