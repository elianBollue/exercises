import sys
import re

for filename in sys.argv[1:]:
    with open(filename, 'r') as file:
        replaced = re.sub(r'#.*$', '', file.read(), flags=re.MULTILINE)
    with open(filename, 'w') as newfile:
        newfile.write(replaced)