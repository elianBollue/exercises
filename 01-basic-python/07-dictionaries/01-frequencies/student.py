# Write your code here
def frequencies(xs):
    result = {}
    for x in xs:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1
    return result