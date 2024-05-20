from statistics import mean

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average = {}

students_list = sorted(students)
for i in range(len(students_list)):
	arithmetic = mean(grades[i])
	average[students_list[i]] = arithmetic

print(f'Студенты и их средний бал:\n{average}')
