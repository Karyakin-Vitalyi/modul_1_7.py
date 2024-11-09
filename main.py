
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
print(type(grades))
print(grades [0])
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(type(students))
res = sorted(students) #  выстроили множество students  по алфавиту
print("Список по алфавиту:")
print(res)

import statistics
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# average = sum(grades[0) / len(grades[0]), sum(grades[1) / len(grades[1]), sum(grades[2) / len(grades[2]), sum(grades[3]) / len(grades[3)
# print(average)
# # average = statistics.mean(grades[0::])
# # print(average)
# Вычисление среднего значения для каждого списка
average = [sum(sublist) / len(sublist) for sublist in grades]

# Вывод среднего значения
print("Среднее значение для каждого списка:")
print(average)
print(dict(zip(res,average)))