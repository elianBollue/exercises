# Write your code here
def countdown(n):
    dezeTuple = (str(k) for k in range(n,0,-1))
    return ", ".join(dezeTuple)