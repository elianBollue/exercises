# Write your code here
def median(ns):
    xs = sorted(ns)
    i = len(ns) // 2
    if len(ns)%2 == 0:
        return (xs[i] + xs[i-1])/2
    else:
        return xs[i]