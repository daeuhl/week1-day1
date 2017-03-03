#!/usr/bin/env python3

number_of_assessments = 3

grade_weight = 0

print('\n' + "Hess\'s Anvil" + '\n')

student = str(input('What is the student\'s name? '))

phase_1_assessment_raw_score = float(input('What grade did ' + \
                                student + ' earn, on their ' + \
                                'first exam? '))
phase_2_assessment_raw_score = float(input('What grade did ' + \
                                student + ' earn, on their ' + \
                                'second exam? '))
phase_3_assessment_raw_score = float(input('What grade did ' + \
                                student + ' earn, on their ' + \
                                'third exam? '))

sum_of_raw_scores = phase_1_assessment_raw_score + \
                    phase_2_assessment_raw_score + \
                    phase_3_assessment_raw_score

raw_score = float(sum_of_raw_scores / number_of_assessments)

great_filter = str(input('Did ' + student + " use an " + \
                'integrated development environment instead of a ' + \
                'text editor? '))

acceptable_answers = ['yes', "no"]

if great_filter.lower() in acceptable_answers:
    if great_filter.lower() == "yes":
        final_grade = float(raw_score * grade_weight)
        print('\n' + student + "\'s grade: " + str(final_grade) + '\n')
    else:
        grade_weight = 1
        final_grade = float(raw_score * grade_weight)
        print('\n' + student + "\'s grade: " + str(final_grade) + '\n')
else:
    print('It\'s a yes-or-no question.' + "\n")