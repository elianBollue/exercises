# Write your code here
def slug(fullname):
    words = fullname.split()
    achternaam = words[1:]
    voornaam = words[0]
    return "-".join(deel.lower() for deel in achternaam + [voornaam])