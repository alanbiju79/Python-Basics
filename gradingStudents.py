#This program rounds student grades.
#If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
#If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.

import os
import sys

def gradingStudents(grades):

    for i in range(len(grades)):
        if grades[i] < 38:
            grades[i] = grades[i]
            
        else:
            if (grades[i] + 1) % 5 == 0:
                grades[i] = grades[i] + 1
                
            elif (grades[i] + 2) % 5 == 0:
                grades[i] = grades[i] + 2
                
            else:
                grades[i] = grades[i]
        
    return grades    
    

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
