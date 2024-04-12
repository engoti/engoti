num_students=int(input('How many students do you have? '))

num_test_scores=int(input('How many test scores per student? '))

for student in range(num_students):
    total=0
    print('Student number', student+1)
    print('-------------------')
    for test_num in range(num_test_scores):
        print('Test number', test_num + 1, end='')
        score = float(input(': '))
        total+= score

    average= total / num_test_scores

    print('The average for student number', student + 1,
          'is: ', average)
    print()