# Write your code here
#def sum_squares(ns):
#    squares = []
#    for n in ns:
#        squares.append(n ** 2)
#    return sum(squares)

def sum_squares(ns):
    return sum([ n ** 2 for n in ns ])