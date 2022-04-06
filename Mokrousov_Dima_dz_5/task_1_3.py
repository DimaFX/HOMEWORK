tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Елена', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

gen = ((tutor, klass) for tutor, klass in zip(tutors, klasses))
print(next(gen))
print(list(gen))

from itertools import zip_longest


if len(tutors) >= len(klasses):
     gen = ((tutor, klass) for tutor, klass in zip_longest(tutors, klasses))
else:
     raise Exception('Список tutors меньше чем список klasses')
print(next(gen))
print(list(gen))