# Write your code here
def is_increasing(ns):
    zipped = zip(ns,ns[1:])
    return all(x <= y for x,y in zipped)