# Write your code here
def nth_longest_string(n,strings):
    strings = sorted(strings, key=len)
    return strings[-n]