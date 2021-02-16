# Write your code here
def remove_duplicates_lists(xs): # for those ultra slow speeds
    newList = []
    for x in xs:
        if x not in newList:
            newList.append(x)
    return newList

def remove_duplicates(xs):
    check = set()
    newList = []
    for x in xs:
        if x not in check:
            newList.append(x)
            check.add(x)
    return newList