import students_lib
import grades



for student in students_lib.students:
    if student['active']:
        print(student['name'])
        for grade, min_score in grades.grade_rule.items():
            if student['score'] >= min_score:
                student['grade'] = grade
                break

print(students_lib.students)