# Write your code here
def format_grades(grades):
    def gem(ns):
        return round(sum(ns)/len(ns))

    dezeLijst = (f'{name}: {gem(grades)}' for name, grades in grades.items())
    return "\n".join(dezeLijst)