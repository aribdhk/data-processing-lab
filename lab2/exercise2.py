#exercise2
grades=[24,30,49,43,70]
print(len(grades))
print(max(grades))
def grade_calculator(grades):
    total_grade=sum(grades)
    average_grade=(grades/(len(grades)))
    highest_grade=max(grades)
    lowest_grade=min(grades)
