# Write your code here
def coins(one,two,five,goal):
    for een in range(one+1):
        for twee in range(two+1):
            for vijf in range(five+1):
                if een + 2*twee + 5*vijf == goal:
                    return True
    return False