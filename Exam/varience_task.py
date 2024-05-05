import numpy as np

# Вероятности попадания в каждую из мишеней для каждого типа винтовки
probabilities_with_scope = np.array([0.7, 0.15, 0.1, 0.05])
probabilities_without_scope = np.array([0.4, 0.3, 0.2, 0.1])

# Количество очков, которое дает каждая мишень
scores = np.array([50, 30, 20, 10])

# Вероятность выбора винтовки с оптическим прицелом и без него
p_scope = 6 / 10
p_no_scope = 4 / 10

# Математическое ожидание количества очков за один выстрел
expected_score = 5 * (p_scope * np.sum(probabilities_with_scope * scores) + 
                      p_no_scope * np.sum(probabilities_without_scope * scores))

# Вероятность набрать максимальное количество очков
p_max_score = (p_scope * probabilities_with_scope[0] + 
               p_no_scope * probabilities_without_scope[0]) ** 5

print(f"Математическое ожидание количества очков Васи в соревновании: {expected_score}")
print(f"Вероятность того, что Вася наберет максимальное количество очков: {p_max_score}")