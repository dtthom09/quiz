print('Dylan\'s Quiz'
      '')


answer = input('Are you ready!? (yes/no): ')
score = 0
questions = 5

if answer.lower() == 'yes':
    answer = input('1. What is the city that keeps the roof blazin? ')
    if answer.lower() == 'mia' or answer.lower() == 'miami' or answer.lower() == 'miaaami':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    answer = input('2. What is -4+4? ')
    if answer == '0' or answer.lower == 'zero':
        score += 1
        print('Correct!')
    else:
        print('really?...wrong!!!')

    answer = input('3. What is the best programming language? ')
    if answer.lower() == 'python':
        score += 1
        print('There\'s no debating this!')
    else:
        print('In your dreams!')

    answer = input('4. What is the best type of income? ')
    if answer.lower() == 'passive' or answer.lower() == "passive income":
        score += 1
        print('Correct!')
    else:
        print('Not even close!')

    answer = input('5. If you are standing somewhere and you walk a mile south, a mile west, and then a mile north '
                   'and you end up in tha same place, where are you? ')
    if answer.lower() == 'north pole' or answer.lower() == "the north pole" or answer.lower() == 'south pole' or answer.lower() == 'the south pole' or answer.lower() == 'one of the poles':
        score += 1
        print('Correct!')
    else:
        print('Incorrect')

    per = score / questions * 100
    print('Thanks for playing! Score: ', per, '%')
    if per > .55:
        print('You passed!!')
    else:
        print('Maybe next time!')

else:
    print('Why the hell not?')


