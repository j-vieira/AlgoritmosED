grades = [84,29,57,39,40,74,83]
multipleGrades = []
tempGrade = 0
remainder = tempGrade % 5 


for i in range(0, len(grades)):
    tempGrade = grades[i]
    while tempGrade % 5 != 0:
        tempGrade += 1
    
    if(grades[i]>=40 and tempGrade-grades[i]<3):
        multipleGrades.append(tempGrade)
    else:
        multipleGrades.append(grades[i])

print(multipleGrades)
